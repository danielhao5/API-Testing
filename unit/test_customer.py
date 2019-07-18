import stripe
import json 
import os
import pytest


stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
print('------------------------------------')
print('----Testing Customer API ----------- ')
# test customer realated API

def test_create():
    global customer_id
    customer = stripe.Customer.create(
                                email='mike.lee@example.com',
                                source='tok_amex')

    customer_id = customer['id']
    #print(f' customer crated.  id: {customer_id}')

    assert customer 
    assert customer_id

def test_create_duplicate():
    ''' new customer has unique id, even has the same info'''
    customer2 = stripe.Customer.create(
                                    name='mike.lee@example.com',
                                    source='tok_amex')
    customer2_id = customer2['id']
    #print(f' customer2 id: {customer2_id}')
    assert customer2_id != customer_id

def test_retrieve():
    customer_obj = stripe.Customer.retrieve(customer_id)

    assert customer_obj['id'] == customer_id

def test_update_after_create():
    '''modify some metadata of an existing customer'''
    order_num = '6665'
    customer = stripe.Customer.modify(customer_id,
                                    metadata={'order_id': order_num})
    order_id = customer['metadata']['order_id']
    assert order_id == order_num 
    

def test_delete():
    '''test delete also serves as the clean-up of resource'''
    response = stripe.Customer.delete(customer_id)
    assert response['deleted'] == True 


@pytest.mark.xfail(strict=True)
def test_update_after_del():
    '''expected case failed - operate on a deleted customer'''
    try:
        stripe.Customer.modify(customer_id,
                               metadata={'order_id': '6665'}) 

    except stripe.error.InvalidRequestError as e:
        '''simple check to verify the exception occurence'''
        print('InvalidRequestError:')
        assert not e 
             
@pytest.mark.xfail(strict=True)
def test_create_failed():
    '''Expect failure - if use the bad card info to create a customer'''
    '''more elaboarte on the error message and handling ''' 

    try:
        stripe.Customer.create(source='tok_InvalidCard')
        
    except stripe.error.StripeError as e:
        body = e.json_body
        err = body.get('error', {})
        err_msg = err.get('message')

        print("Status is %s" % e.http_status)
        print("Code is: %s" % err.get('code'))
        print("Error Message: %s" % err_msg)
        assert err_msg != 'No such token: tok_InvalidCard'

    except Exception as e:
        print(e)
        pass
