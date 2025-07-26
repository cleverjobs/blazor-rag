# Access Grid Data for Grid's GroupHeaderTemplate

## Question

**Bri** asked on 07 Jul 2022

OBJECTIVE: As I know the <GroupHeaderTemplate> is not directly associated with the data therefore I cannot establish a context for DTOs. I wish you access the data collection and display data dynamically using the <GroupHeaderTemplate>. In this case I want to showcase days of the week along side the date based on the data in my DTOs rather than the default that is given from DateTime. QUESTION: How would I go about displaying dynamic data in a <GroupHeaderTemplate> the same way it is done in other Telerik Templates? Below is the relevant code the produces my question.

## Answer

**Brian** answered on 07 Jul 2022

My Solution: I solved this by adding a DateOnly Field to my DTO for strictly grid UI purposes, taking the @context.Value in the <GroupHeaderTemplate> and casting the object from the <GroupHeaderTemplate> context to a nullable (which in my case is fine) DateOnly. I had to do this grouping because DateTime breaks everything up down to milliseconds therefore grouping for only dates did not work due to the Member being matched to the <GridColumn Field> parameter. I added a non-visible column DateOnly and OnStateInit loaded my GroupDesciptor MemberType as a DateOnly and Member to the DTO field I made. This correctly grouped the Dates wile also allowing me to manipulate the group header information since it was able to recognize the non-visible column I create. Regards: If anyone is having issues I advise you to remember that the @context.Value is an object you must cast that value to what is necessary for your scenario. Make sure your <GridColumn Field=" nameof (@YOUR_DTOFIELD_HERE )"/> matches your manually loaded GroupDesciptor to ensure Telerik's logic knows what column it is working with. If you are confused about nameof travel to this link here to learn the nameof expression.
