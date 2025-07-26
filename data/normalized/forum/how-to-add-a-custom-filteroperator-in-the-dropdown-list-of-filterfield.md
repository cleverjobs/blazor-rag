# How to add a Custom FilterOperator in the dropdown list of FilterField

## Question

**Fab** asked on 03 Mar 2022

Good morning all, I'm taking a look to the new Filter component, recently added to Telerik UI for Blazor. I'm using it to build conditions to send to a custom SQL Query generator which will build the where clauses mapping from the export of the filter component. You can see my previous question (edited after i figured out a way) here: [https://www.telerik.com/forums/how-to-use-the-new-filter-component-to-create-an-sql-query](https://www.telerik.com/forums/how-to-use-the-new-filter-component-to-create-an-sql-query) The main reason I'm writing you is because I need to add custom items in the list of operators. Specifically to check an Item against a list, but it's irrelevant I just need an operator that would then be interpreted by the QueryBuilder, I don't need to integrate with other telerik components. Can I extend some of Telerik classes to implement the functionality I need? Is there any way? If this is possible in any other way, can you point me in the right direction? Thank you very much PS: I tagged this question as General Discussion as it seems like a "Filter" tag is not available yet. Have a nice day! FB Thanks, have a nice day.

## Answer

**Joana** answered on 08 Mar 2022

Hi Fabrizio, Our Filter component is bound to a FilterDescriptor that support only the predefined set of filter operators (through the FilterOperator enum). The component is designed like this to integrate with our Telerik.DataSource. The purpose of our datasource is to facilitate our customers by performing queries on the data for filtering, sorting, etc. Thus, custom filtering operators in the Filter component are not supported out-of-the-box because it will break the integration with our datasource. As you are serializing and building your own query generator, I think that there might be a potential workaround. You can customize the Operators collection through the parameter. In the collection you might use a built-in filter operator, but later replace it with the operator that you would like in the serialized json. Below you can find our demos for custom operator list: [https://demos.telerik.com/blazor-ui/filter/operators](https://demos.telerik.com/blazor-ui/filter/operators) <TelerikFilter @bind-Value="@Value"> <FilterFields> <FilterField Name="FirstName" Type="typeof(string)" Label="First Name" Operators="@NameOperators" /> </FilterFields> </TelerikFilter> @code {
public CompositeFilterDescriptor Value { get; set; }=new CompositeFilterDescriptor();

public List <FilterListOperator> NameOperators { get; set; }=new List <FilterListOperator> ()
{
new FilterListOperator { Operator=FilterOperator.StartsWith, Text="begins with" },
new FilterListOperator { Operator=FilterOperator.EndsWith, Text="ends with" }
};
} Regards, Joana Progress Telerik
