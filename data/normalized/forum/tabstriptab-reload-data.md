# TabStripTab reload data

## Question

**HYO** asked on 29 Nov 2021

Hello, Excuse the bad English There is telerikgrid, and when I click Row on that grid, I load the razor page in tabstriptab with grid data as a parameter. I want the contents of the razor page to change based on the parameter value that changed when I clicked row on the grid. Currently, the parameter value changes, but the razor page does not reload. What Should I do? Here is the detail code: <TelerikTabStrip @bind-ActiveTabIndex="@ActiveTabIndex"> <TabStripTab Title="Drawing"> <Drawing DCT_NO="@DctNo" ENV_NO="@PartNo" ENV_TYPE="@EnvType" ENV="@ENV" COID="@COID"> </Drawing> </TabStripTab> <TabStripTab Title="Cad"> <Cad DCT_NO="@DctNo" ENV_NO="@PartNo" ENV_TYPE="@EnvType" ENV="@ENV" COID="@COID"> </Cad> </TabStripTab> </TelerikTabStrip> Thank you.

## Answer

**Marin Bratanov** answered on 29 Nov 2021

Hello, Typically, to re-render a component you need to update the data in its view-model, and for components you do not re-initialize, the typical place is the OnParametersSetAsync event. It fires when parameters change and that can let you get new data. It is also important to note that collections trigger that event only when their reference changes, not when their items change (see more on that here ). Regards, Marin Bratanov

### Response

**HYOKYEONG** commented on 29 Nov 2021

Marin, thank you for your answer. However, the razor file still does not re-render. The razor file I need to re-render has telerik grid, which uses OnRead event. As a result of switching to OnParametersSetAsync(), I have confirmed that if the parameter changes, the code in OnParametersSetAsync() method will be excuted, but not in ReadItems() method. Is there a way to run the ReadItems() method every time the parameter changes? <TelerikGrid Data="@GridData" TotalCount="@Total" OnRead="@ReadItems"> </TelerikGrid> Thank you.

### Response

**Marin Bratanov** commented on 01 Dec 2021

The situation you have seems to not change a parameter on the grid itself, so the grid won't re-render and fire OnRead. What you can do is to cache the current DataSourceRequest object and extract the logic that uses it to fetch data into a separate method that you can call from OnParametersSetAsync (only on subsequent updates). You can find a similar scenario in the article for the OnRead event, see the "Cache Data Request" section.
