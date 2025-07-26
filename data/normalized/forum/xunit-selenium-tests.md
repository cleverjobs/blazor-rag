# xUnit & Selenium Tests

## Question

**Sim** asked on 19 Nov 2020

I am trying to create some end-to-end automation tests for the grid using Selenium WebDriver. I cannot seem to find out how to access the grids data without just treating it as a html table. I would like to be able to check the search box, filters, grouping etc are all working.... is this possible or do I have to buy Telerik's Test Studio?

## Answer

**Dimitar** answered on 19 Nov 2020

Hi Simon, Blazor can be successfully automated with both Selenium WebDriver and Telerik Test Studio. Test Studio provides some useful abstractions of Blazor components that can make it much easier for testing. If you decide to use WebDriver you may want to implement such abstractions by yourself. Once you have those abstractions you can reuse them in any project you have. Regards, Dimitar

### Response

**Simon** answered on 20 Nov 2020

Hi Dimitar thanks for the response. The issue for me is I am not able to convince my company to purchase the Test Studio due to the very uncertain times we find ourselves in at the moment. So I am trying to automate the testing without Studio, however I don't understand how I can access the grid inside a test. I can get the currently visible data on the page by treating the grid just like an html table like this: [Fact] public void SearchGridForText() { Driver.Navigate() .GoToUrl(HotfixHistoryUrl); var gridContainer=Wait.Until(SeleniumExtras.WaitHelpers.ExpectedConditions.ElementExists(By.Id( "hotfixGridContainer" ))); Assert.NotNull(gridContainer); var rows=gridContainer.FindElements(By.TagName( "tr" )); Assert.NotEmpty(rows); foreach (var row in rows) { _testOutputHelper.WriteLine(row.Text); } } This way does not give me access to the grid component nor the whole dataset. What I would really like is to create end-to-end testing to validate the grid is loading data, filters and search are working properly etc So I guess my question is can I do this with the WebDriver or do I need the Test Studio? Hope that all makes sense, thanks for your time Simon

### Response

**Dimitar** answered on 20 Nov 2020

Hi Simon, Telerik's Blazor components provide productivity for developers. In the same way, TestStudio provides productivity for people who develop test automation. All the abstractions that TestStudio provide can be implemented in WebDriver, there are no technical limitations. Here is an example of how you can access grid cells: gridContainer.FindElement(By.CssSelector( ".k-master-row:nth-of-type(3) td:nth-of-type(3)" )) This will return the cell on the 3rd row and 3rd column. Another example of how you can find the number of items in the grid: gridContainer.FindElement(By.CssSelector( ".k-pager-info" )).Text It will return the text of the pager's info element. Regards, Dimitar

### Response

**Marin Bratanov** answered on 29 Mar 2021

Hello all, Since you expressed interest in testing with Selenium, you may find interesting this request: [https://feedback.telerik.com/blazor/1513117-translators-for-selenium-testing-for-the-telerik-ui-for-blazor-components.](https://feedback.telerik.com/blazor/1513117-translators-for-selenium-testing-for-the-telerik-ui-for-blazor-components.) If so, Vote for it and Follow it so we can know there is interest, and so you can get status updates. Regards, Marin Bratanov Progress Telerik
