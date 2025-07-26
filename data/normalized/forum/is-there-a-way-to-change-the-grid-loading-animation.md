# Is there a way to change the Grid loading animation?

## Question

**Dou** asked on 22 Aug 2022

the built in Grid loading animation appears to default to k-loader-spinner-3. How can I change this to k-loader-spinner-4 to match the loading animation in the rest of my application?

## Answer

**Dimo** answered on 24 Aug 2022

Hello Doug, I have to admit that there is no setting for changing the Grid's loading animation. What you can do is disable the built-in Grid loading animation and use a separate LoaderContainer in combination with a Grid OnRead handler, which will allow you to know when a request is made. Regards, Dimo

### Response

**Doug** commented on 24 Aug 2022

Thank you, Dimo.
