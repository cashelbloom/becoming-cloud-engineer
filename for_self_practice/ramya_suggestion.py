books = {'storyBook': 10.5, 'textBook': 12.0, 'scientificBook': 25.75, 'magazine': 3.25}

subscription = {'storyBook': True, 'magazine': False, 'textBook': True}

def compute_subscription_cost():
    subscription_cost = 0.0
    for k,v in subscription.items():
        if v == True:
            subscription_cost += books[k]
    print(f'This is the cost of your subscription choice: {subscription_cost}')


compute_subscription_cost()