# How you have solved filtering a grid on property that is a collection

## Question

**ale** asked on 01 Mar 2024

My scenario is that I have a grid of User. a User has Roles. I have a column that I have used the <Template> to display a chip of each Role a User has. The FilterTemplate does not have a solution to filter this collection out of the box. Have you solved this or similar? Please share any helpful feedback here as I am blocked on this task. I would prefer not to filter on a concatenated string of the users roles, as if I click the filter checkbox 'Admin' it would show results for any role that had Admin in it's name. If you used the OnRead event, when did you apply your filter and how? Thanks so much for your feedback on how you've solved this for your use case.

## Answer

**Nadezhda Tacheva** answered on 01 Mar 2024

Hi Alex, I already responded in your private ticket but I am adding the information here as well, so it is available for other interested community members. One can allow filtering of a column that contains a collection of items with a custom approach. Guidelines and an example can be found here: Filter a Grid Column that is a List. Regards, Nadezhda Tacheva Progress Telerik

### Response

**alex** commented on 05 Mar 2024

Hi Nadezhda thanks for your response, this example is very helpful :)
