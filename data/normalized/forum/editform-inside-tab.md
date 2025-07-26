# EditForm inside Tab

## Question

**BobBob** asked on 14 Sep 2020

Is it not possible to use an EditForm inside of a tab? When I try, I am getting: System.InvalidOperationException: EditForm requires a Model parameter, or an EditContext parameter, but not both. <TelerikTabStrip @bind-ActiveTabIndex="activeTabIndex"> <TabStripTab Title="Information"> <EditForm Model="@ticket" OnValidSubmit="@UpdateTicket"> </EditForm> </TabStripTab> <TabStripTab Title="Time Entry"> </TabStripTab> <TabStripTab Title="History"> </TabStripTab> </TelerikTabStrip>

## Answer

**Svetoslav Dimitrov** answered on 15 Sep 2020

Hello Bob, I have prepared a sample application which has a Telerik TabStip with a basic example of EditForm. You can see that project as an attached file. Could you run it locally and if it works as expected for you, compare it against your own and see what are the differences that cause the issue. If this does not help you move forward, could you modify the application so that the exception is reproducible and send it back to us so we can dive deeper and suggest another solution? Regards, Svetoslav Dimitrov

### Response

**Bob** answered on 15 Sep 2020

I found my problem, thanks. The error was misleading. The problem was actually in the data I was getting back.
