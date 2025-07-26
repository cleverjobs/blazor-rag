# How to filter Grid on a column that is a list?

## Question

**Jas** asked on 07 Jun 2021

I populate the Grid with ~5000 results from a database. The Grid does the paging, sorting, and filtering in memory, except it won't filter for this one column that is a List<string> CustomerNamesList. I'm attempting to use the FilterMenuTemplate -- I just need a textbox and a dropdown like "Contains" and "Does Not Contain" but I can't figure out how to filter the Grid. <GridColumn Field="@(nameof(CustomerNamesList))" Title="Customers" Sortable="false" Filterable="true"> <FilterMenuTemplate> <label for="NameMenuFilter"> Customer Name: </label> <TelerikTextBox Id="NameMenuFilter" ValueChanged="@((value)=> UpdateCustomerNameFilter(value))"> </TelerikTextBox> </FilterMenuTemplate> <Template> @* display - loop thru List of customer names *@</Template> </GridColumn> This code gets hit, but it's not doing anything... public void UpdateCustomerNameFilter(string itemValue)
{
var filter1=partyNamesFilterContext.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor;
filter1.Value=itemValue;
filter1.Operator=FilterOperator.Contains;
} When I click Filter, it gives me a blazor.server.js error Error: System.ArgumentException: Provided expression should have string type (Parameter 'stringExpression') Update Here's what I'm using as the datasource to make things clearer: IEnumerable<Companies> So what it appears to me is that the Grid doesn't know how to filter on a List of objects like this List<string> public class Companies { public int Id {get; set;} public List <string> CustomerNamesList {get; set;}=new List <string>(); // Other fields
}

## Answer

**Hristian Stefanov** answered on 10 Jun 2021

Hi Jason, I tried to reproduce the described scenario on my end. It seems I cannot get the same result. The problem might come from those little parts missing (like the Template content) from the provided example. I have also changed a little bit the Filed of the column from "@(nameof( CustomerNamesList) )" -> "@(nameof( Sample.CustomerNamesList ))", but this might be just a typo. In order for me to be on the same page as you, could you please try to send me a little reproduction or a little more code snippets? This will be really helpful for us, and I will be able to investigate further. By the way, you can see an example of an approach using FilterMenuTemplate in our demo here: [https://demos.telerik.com/blazor-ui/grid/custom-filter-menu.](https://demos.telerik.com/blazor-ui/grid/custom-filter-menu.) You may find really useful additional information about your case. Thank you. Regards, Hristian Stefanov Progress Telerik

### Response

**Jason** commented on 10 Jun 2021

I've updated the question to make source clearer. I'm trying to filter on a list of strings, so I'm wondering if that is supported or not. The examples all use predefine types like String, Int, Date, and Bool.

### Response

**John** commented on 11 Jun 2021

I'd also like to know if there's a recommended way to filter a column with a list<string> in it.

### Response

**Hristian Stefanov** answered on 14 Jun 2021

Hello Jason, I apologize for the misunderstanding. You are correct that in a Grid column field we support only the predefined types like the ones we use in our examples (string, int, date, bool..). This is the reason that causes a System.ArgumentException error. The desired result can be achieved with the following approaches: Use the OnRead event to perform the filtering inside of it. This will let you customize your filter. Use the FilteMenuTemplate like in the demo from my previous answer. I hope this helps. If you have any other questions, please let me know. Regards, Hristian Stefanov Progress Telerik

### Response

**Jason** commented on 14 Jun 2021

Thanks for that confirmation. But you are saying it IS possible to have Telerik Grid filter a List<string> in either approach? I understand OnRead allows me to go retrieve a newly filtered result from the database or even in memory, but I was hoping we could get Telerik to do its own filtering. I would be intrigued if I could do it using FilterMenuTemplate to filter the List<string>, but your demo only shows using string, int, date, bool. The example shows the use of FilterDescriptors and I'm wondering if I'm only a couple lines of code away from filtering on a List<string> ?? My only viable option right now is to get rid of the List<string> which reduces the usefulness of the Grid.

### Response

**David** commented on 24 Mar 2022

I have this exact same need and can't figure it out either.

### Response

**Marin Bratanov** commented on 26 Mar 2022

There isn't a built-in solution for this, as there isn't one in the framework. Comparison is not defined for collections and so we can't execute a filter or sort on anything but primitive (value) types. You can read more about this and a few other notes here: [https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes](https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes) So, you will need to implement that specific filtering entirely in the business application code and I can't say what the best way to do that is, as it depends heavily on the situation. What the grid gives you is: filter template so you can get the proper UI for collecting the info you need from the user the OnRead event that fires with filters you can create based on that information so you can implement the needed data source operations in your app/service/database (generally - code)

### Response

**Dimo** answered on 12 Sep 2023

Hi all, For anyone who is interested in filtering a list property in the Grid, please refer to the linked knowledge base article. Regards, Dimo Progress Telerik
