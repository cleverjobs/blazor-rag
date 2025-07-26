# ui for blazor bind-Value

## Question

**kha** asked on 15 Dec 2019

Hello , i was wondering if i can choose bind-Value event for each component like blazor it self ( @bind-value:event )

## Answer

**Marin Bratanov** answered on 15 Dec 2019

Hello, This is not possible for our components because they don't have the simplistic rendering the ones coming from the framework have. It would not even make sense for most of the components such as the dropdowns and the date/time pickers. For the inputs, if you want to use a slower cadence of changes, I suggest you hook to their OnChange event and update the model with your code in the event handler. Regards, Marin Bratanov
