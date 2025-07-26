# How to set the Telerik ListView to horizontal

## Question

**Eri** asked on 19 Apr 2024

I have been searching thru the forum and online and cannot figure out how to set the TelerikListView component to display the items in the itemtemplate horizontally. I see there is a ListViewSettings but I can't find any documenation on what to put into the settings.

## Answer

**Hristian Stefanov** answered on 19 Apr 2024

Hi Eric, To display the ListView items horizontally, apply the " display: inline-block; " CSS style to the " k-listview-item " HTML div element. Here is an example I have prepared for you: <style>.k-listview-item { height: 150px; width: 150px; display: inline-block; margin: 10px; border: 1px solid black; border-radius: 10px; padding: 10px;
} </style> <TelerikListView Data="@ListViewData" Width="700px" Pageable="true" PageSize="4"> <HeaderTemplate> <h2> Employee List </h2> </HeaderTemplate> <Template> <h4> @context.Name </h4> <h5> @context.Team </h5> </Template> </TelerikListView> @code {
private List <SampleData> ListViewData { get; set; }=Enumerable.Range(1, 25).Select(x=> new SampleData
{
Id=x,
Name=$"Name {x}",
Team=$"Team {x % 3}"
}).ToList();

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
}
} Please run and test it to see the result. Regards, Hristian Stefanov Progress Telerik

### Response

**Eric** commented on 19 Apr 2024

Thanks Hristian. That leads me to another question. Is there a list of what css class names belong to what telerik controls? How would one know what css classes are used? I built our css with themebuilder but don't see anywhere in that which spells out all of the css classes used for each control and its elements. I would have never know that the class was k-listview-item

### Response

**Hristian Stefanov** commented on 22 Apr 2024

Hi Eric, Thank you for getting back to me with feedback. Let me shed some light on the CSS classes documentation question below. Documentation about the k-classes is rarely needed. Normally, a developer will create a custom theme with our Blazor ThemeBuilder to use a different color scheme. This process does not require knowledge about the k-classes. Advanced customization may involve changing the components' sizing, but the k-classes don't participate in this process either. Which leaves just one case when these classes are needed - when you need to tweak a specific element in a specific way. The easier way to do this is to open the browser's web inspector, see what is the CSS class and current styles, and create a custom CSS rule to apply different styles. The number of possible scenarios here is unlimited, so I can't imagine documentation that can be specific and useful enough. Nevertheless, if you share what type of documentation you expect and how you intend to use it, we will consider adding it. Kind Regards, Hristian
