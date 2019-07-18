import stripe
import os
import pytest

active = 'False'

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
print('-----------------------------------')
print('------Testing Product API --------- ')

def test_create():
    global product_id
    product = stripe.Product.create(type='service', name='Green Lawn')
    product_id = product['id']
    assert product 
    assert product_id

def test_retrieve():
    product_obj = stripe.Product.retrieve(product_id)
    assert product_obj['id'] == product_id

def test_update():
    '''expected active status changes - operate on an existing product'''
    product = stripe.Product.modify(product_id,
                                    active=active,)
    status = product['active']
    assert status == False

def test_list():
    '''list the inactive product by product id '''
    product=stripe.Product.list(active=active)
    product_ID = product['data'][0]['id']

    assert product_ID == product_id

def test_delete():
    '''test delete also serves as the clean-up of resource'''
    response = stripe.Product.delete(product_id)
    assert response['deleted'] == True 

@pytest.mark.xfail()
def test_update_after_del():
    '''expected case failed - operate on a deleted product'''
    try:
        stripe.Product.modify(product_id, 
                    name='Golden Lawn Services')
    except stripe.error.InvalidRequestError as e:
        body = e.json_body
        err  = body.get('error', {})
        err_code = err.get('code')
        err_status = e.http_status

        print('Status is: %s' % err_status)
        print('Error Code is: %s' % err_code)
        ''' compare the error message, should be the same'''
        ''' here did it on pupose to demo the xfail'''
        ''' html report will show the detail trace info.'''
        assert "resource_missing" != err_code

    except Exception as e:
        ''' other type of errors'''
        print(e)
        pass 

    
