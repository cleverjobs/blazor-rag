# Is there a way to change or change or enlarge treelist expand icon?

## Question

**EdEd** asked on 04 May 2021

THanks ... Ed

## Answer

**Marin Bratanov** answered on 04 May 2021

Hello Ed, You can use CSS to do both - just target the built-in font icon to increase its font-size and, optionally, to change the symbol or even font. Here's an example I made for you: <style> /* change size */.my-own-expand-icon td [role='gridcell' ].k-icon::before { font-size: 32px;
} /* change icon */.my-own-expand-icon td [role='gridcell' ].k-icon.k-i-collapse::before { content: "\e00e";
}.my-own-expand-icon td [role='gridcell' ].k-icon.k-i-expand::before { content: "\e00d";
}
</style>

<TelerikTreeList Data=@TreeListData Class="my-own-expand-icon" Pageable="true" Sortable="true" Resizable="true" Reorderable="true" FilterMode="@TreeListFilterMode.FilterMenu" Width="900px" Height="400px" IdField="Id" ParentIdField="ParentId">
<TreeListColumns>
<TreeListColumn Expandable="true" Field=@nameof(Customer.FirstName) Title="First Name" Width="115px" />
<TreeListColumn Field=@nameof(Customer.LastName) Title="Last Name" Width="105px" />
<TreeListColumn Field=@nameof(Customer.CompanyName) Title="Name" />
<TreeListColumn Field=@nameof(Customer.HasCompanyContract) Title="Has Contract" Width="115px" />
<TreeListColumn Field="@nameof(Customer.Email)" Title="Email"></TreeListColumn>
<TreeListColumn Field="@nameof(Customer.Phone)" Title="Phone" Width="120px"></TreeListColumn>
<TreeListColumn Field="@nameof(Customer.City)" Title="City" Width="100px"></TreeListColumn>
<TreeListColumn Field=@nameof(Customer.Id) Title="UserID" />
<TreeListColumn Field=@nameof(Customer.PasswordHash) Title="Pass Hash" Width="100px" />
</TreeListColumns>
</TelerikTreeList>
@code { public List <Customer> TreeListData { get; set; } public class Customer {
public int Id { get; set; } public int? ParentId { get; set; } public string PasswordHash { get; set; } public string FirstName { get; set; } public string LastName { get; set; } public string CompanyName { get; set; } public bool HasCompanyContract { get; set; } public string Email { get; set; } public string Phone { get; set; } public string City { get; set; }
}
// generation of dummy data protected override void OnInitialized ()
{
TreeListData=GenerateData();
} List <Customer> GenerateData ()
{
var data=new List<Customer>();
string[] fNames=new string[] { "Nancy", "John", "Orlando", "Jane", "Bob", "Juan" }; string [] lNames=new string [] { "Harris", "Gates", "Smith", "Caprio", "Gash", "Gee" }; string [] cNames=new string [] { "Acme", "Northwind", "Contoso" }; string [] cities=new string [] { "Denver", "New York", "LA", "London", "Paris", "Helsinki", "Moscow", "Sofia" }; Random rnd=new Random (); for ( int i=0; i <150; i ++)
{
string fName=fNames[rnd.Next(0, fNames.Length)];
string lName=lNames[rnd.Next(0, lNames.Length)];
string cName=cNames[rnd.Next(0, cNames.Length)];
data.Add(new Customer
{
Id=i,
ParentId=GetParentId(i),
PasswordHash="not shown",
FirstName=fName,
LastName=lName,
CompanyName=cName,
HasCompanyContract=i % 3==0,
Email=$"{fName}.{lName}@{ cName }.com ".ToLowerInvariant (), Phone=$"{rnd.Next(100, 999)} -555- {rnd.Next(100, 999)}", City=cities [rnd.Next(0, cities.Length)] });
} return data;
} int? GetParentId ( int index )
{
if (index % 4==0) return null;
return Math.Abs(index - (index % 4));
} } Regards, Marin Bratanov Progress Telerik

### Response

**James** commented on 19 Jul 2023

Marin is this still correct? I have done exactly what you have explained but it has no effect. I am using the latest version of Telerik Blazor controls (4.3) and .NET 7. Blazor Server. I am using the FluentUI Theme. Thanks Jim

### Response

**Georgi** commented on 21 Jul 2023

Hello James, Modifying the icon by changing the content is still a viable method. The only difference is that the CSS classes have changed. The current class responsible for the expand icon is k-svg-i-caret-alt-down. You could look at the following article for more information on the icon changes between version 3.x.x and 4.x.x. Based on those differences, to change the size of all toggle icons like expand and collapse, use the following CSS: <style>.k-treelist-toggle { width: 32px;
}
</style> An additional change is that while we still support Font Icons, the components have transitioned to using SVG icons, because they scale better, are more usable in different layouts, and provide a larger degree of customization. Let me know if further questions arise Best Regards, Georgi Yanushev

### Response

**James** commented on 26 Jul 2023

Thank you Georgi for the example covering changing the size. Unfortunately I am wanting to change the icon not the size. Specifically change expand icon to 'plus' and collapse icon to 'minus'. A snippet of CSS and where to apply it on the TreeList would be greatly appreciated. Thanks Jim

### Response

**Georgi** commented on 27 Jul 2023

Hi, James, This can be accomplished by applying a CSS rule similar to the following one: <style>.k-master-row.k-svg-i-caret-alt-right svg path {
d: path ( "M288 224V96h-64v128H96v64h128v128h64V288h128v-64H288z" );
}.k-master-row.k-svg-i-caret-alt-down svg path {
d: path ( "M96 224v64h320v-64H96z" );
}
</style> Please note I have simply copied the SVG path attribute directly from our existing Plus and Minus icons. Here is a full list of Icons. I have prepared a REPL example which you could look at to see the final result. Feel free to ask if further questions come up. Regards, Georgi

### Response

**James** commented on 04 Aug 2023

Thank you Georgi. Works perfect. I appreciate you going the extra mile to help me!
