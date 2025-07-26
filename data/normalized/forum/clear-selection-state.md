# Clear selection state

## Question

**Rob** asked on 09 Nov 2020

When an item is selected, I want to clear the selection state so that the item isn't indicated as selected. Note: I do not want to have a default item. How do accomplish this?

## Answer

**Marin Bratanov** answered on 10 Nov 2020

Hi Robert, The DropDownList is akin to a <select> element - it always has to show something. If not a selected item, then a default item whose value is the default of the Value type. I advise that you review the Value Out Of Range section of the docs for more details on that. So, you must add a DefaultText, but you can hide its element from the rendering with CSS so the user does not see it: <style>.k-list-optionlabel {
display: none;
} </style>

@result
<br /> from the model: @MySelectedItem
<br />
<TelerikDropDownList Data="@MyList" OnChange="@MyOnChangeHandler" @bind-Value="@MySelectedItem" DefaultText="Select">
</TelerikDropDownList>

@code { string result; string MySelectedItem { get; set; }="second"; void MyOnChangeHandler ( object theUserInput ) {
result=string.Format( "The user selected: {0}", (theUserInput as string )); MySelectedItem=null; } protected List <string> MyList=new List<string>() { "first", "second", "third" };
} Regards, Marin Bratanov

### Response

**Robert** answered on 11 Nov 2020

Sorry, I didn't make myself clear. It's the indication in the drop down I want to get rid of, the one seen in the attached image.

### Response

**Marin Bratanov** answered on 11 Nov 2020

Hi Robert, My previous snippet does that by changing the Value field to null (the default value for a string which my sample uses) - the bold line in the OnChange handler. Regards, Marin Bratanov

### Response

**Robert** answered on 11 Nov 2020

Using this setup: <TelerikDropDownList Data="@MyList" TItem="string" TValue="string" /> I get the initial state seen i image 1, which is also the state I want to have after something has been selected in the drop down, but what I get is what can be seen in image 2. Your example results in what is seen in image 3 (MySelectedItem not initially set to anything) both initially and after selecting something, which is actually worse.

### Response

**Marin Bratanov** answered on 11 Nov 2020

Hello Robert, Can you implement the desired functionality with a <select> element? Once you do that, you should be able to migrate the same data and Value binding (which is missing form the last code snippet) to the Telerik DropDownList. The key thing about this component (and most other inputs) is that they operate over the Value they receive, so it must be set to something, and you also control what they show through this Value by altering the field in your view-model. A dropdown selects (or highlights) the item from its data source that matches the Value you provide to it. That's is key functionality. Not having a selected item means you must set the Value to something that is not in the data source. What I'm seeing in the screenshot also looks a lot like you're attempting to get a SplitButton working, so I'd suggest you Follow the implementation of such a component here: [https://feedback.telerik.com/blazor/1435750-split-button.](https://feedback.telerik.com/blazor/1435750-split-button.) I see you've added your Vote to it already. Regards, Marin Bratanov

### Response

**Robert** answered on 12 Nov 2020

I have followed the implementation of a split button. As image 1 above clearly shows, the dropdownlist can have a state of "nothing selected". The problem is that it cannot go back to it. After selecting an item and then setting the bound value to something that is not in the data source only leads to: * If you have a default text, that item will be selected. * If you don't have a default text, nothing. The item that was selected will remain indicated as selected.

### Response

**Marin Bratanov** answered on 12 Nov 2020

Hello Robert, Please review my initial sample again. It shows how you can provide field in the View-Model to the Value parameter of the component - setting the contents of that field lets you control where there is something selected in the dropdownlist or not. Setting a null value will let it show "nothing". The key thing is that this must trigger a change in the selection once an item has been selected, and this means there must be a matching item in the data source that has that Value. The best way to do that, is to use the DefaultText. Since you don't want that option to be available in the dropdown, I've added a CSS rule for you to hide it. This behavior is identical with the plain <select> element, and the Telerik component can't be expected to behave in a different way. That said, here's another example I made for you that showcases the behavior of the <select> component and how the DefaultText feature of ours enhances things so you can get more flexibiilty. At the end of the post you will also find a short video of the expected behavior and how you can always react to the new value from the Telerik component, while keeping it "selection-free". <style>.k-list-optionlabel {
display: none;
} </style>

@result
<br /> from the model: @MySelectedItem
<br />
<TelerikDropDownList Data="@MyList" OnChange="@MyOnChangeHandler" @bind-Value="@MySelectedItem" DefaultText=" ">
</TelerikDropDownList>

@* with a regular select you cannot even pass the value, it only has @bind or @onchange *@<select @onchange="@SelectOnChangeHandler">
@foreach ( var item in MyList)
{
<option value="@item">@item</option>
}
</select>

@code { string result; string MySelectedItem { get; set; } void MyOnChangeHandler ( object theUserInput ) {
result=string.Format( "The user selected: {0} from the TELERIK component", ( theUserInput as string )); MySelectedItem=null; } protected List <string> MyList=new List<string>() { "first", "second", "third" }; void SelectOnChangeHandler ( ChangeEventArgs e ) {
result=string.Format( "The user selected: {0} from the SELECT component", (e.Value as string ));
MySelectedItem=null;
}
} Regards, Marin Bratanov
