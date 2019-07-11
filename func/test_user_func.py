'''Function case 1 - New Customer onboard, subcribe a plan, charge, and refund
   test the API flow, and abort the subsequent cases if previous one failed'''

import stripe
import os
import pytest 
import pytest_dependency

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@pytest.mark.dependency()
def test_create_user():
    global customer_id
    customer = stripe.Customer.create(
                    email='mike.lee@example.com',
                    source='tok_amex')

    customer_id = customer['id']
    assert customer
    assert customer_id 

@pytest.mark.dependency()
def test_create_product():
    global product_id
    product = stripe.Product.create(name='Green Lawn', 
                                    type='service')
    product_id = product['id']
    assert product
    assert product_id

@pytest.mark.dependency(depends=['test_create_product'])
def test_create_plan():
    global plan_id
    plan = stripe.Plan.create(product=product_id,
                              interval='week',
                              currency='usd', amount='5000')
    plan_id, p_interval = plan['id'], plan['interval']
    assert plan
    assert plan_id 

@pytest.mark.dependency(depends=['test_create_plan'])
def test_subscribe():
    subscription = stripe.Subscription.create(customer=customer_id,
                                              items=[{'plan': plan_id}])
    #print(subscription)
    assert subscription 
   
@pytest.mark.dependency(depends=['test_subscribe'])
def test_charge():
    global charge_id

    charge = stripe.Charge.create(customer=customer_id,
                amount=12000, currency="usd",  
                description="Charge for mike.lee@example.com"
                )
    charge_id = charge['id']
    assert charge
    #assert 0            # 'deliberately failed'

@pytest.mark.dependency(depends=['test_charge'])
def test_refund():
    re = stripe.Refund.create(charge=charge_id, 
                            amount='5000',
                            )             
    assert re


@pytest.mark.dependency(depends=['test_refund'])
@pytest.mark.xfail()
def test_refund_exceed():
    '''expected fail, the refund exceeds the charge amount'''
    re2 = stripe.Refund.create(charge=charge_id,
                               amount='60000')
    
    assert re2

