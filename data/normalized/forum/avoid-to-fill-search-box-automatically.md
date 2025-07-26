# Avoid to fill search box automatically

## Question

**Jih** asked on 27 Apr 2021

Hello, I use Telerik Grid and Search Box. When I clicked edit command in Grid, Search Box is filled automatically. And in my opinion, this value is GridCommandEventArgs. How can I avoid to fill search box automatically? Sincerely, Hanna Lee

### Response

**Marin Bratanov** commented on 28 Apr 2021

Such behavior is not expected and I recommend you open a new support ticket and send us a simple reproducible that we can run and inspect. In the meantime, I suggest you try removing custom code related to the searchbox (e.g., js interop calls that try to clear it or set its value programmatically).
