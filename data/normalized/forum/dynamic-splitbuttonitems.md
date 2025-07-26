# Dynamic SplitButtonItems

## Question

**Lel** asked on 11 Aug 2023

The SplitButton Demo shows how to create a SplitButton with a fixed collection of SplitButtonItems, in that case for "Paste Text", "Paste as HTML", and "Paste Markdown". I need to have a dynamic collection of SplitButtonItems. A common example of this is the undo split button found in many applications such as Visual Studio or Microsoft Word. Clicking the undo icon undoes one step of actions. Or you can click the dropdown and select a step to go back to. The list of options grows in size and changes, based on user actions.

## Answer

**Hristian Stefanov** answered on 15 Aug 2023

Hi Leland, Below, I have crafted an illustrative example for you that showcases dynamic SplitButton options. Feel free to test the sample by selecting any of the buttons. Should you opt for the "Add New Button" option, it will integrate dynamically a new SplitButton into the existing list. <TelerikSplitButton OnClick="@HandleMainBtn"> <SplitButtonContent> Main Button </SplitButtonContent> <SplitButtonItems> @foreach (var splitBtn in splitButtons)
{ <SplitButtonItem OnClick="@(()=> HandleAction(splitBtn))"> @splitBtn </SplitButtonItem> } </SplitButtonItems> </TelerikSplitButton> Last action: <strong> @LastAction </strong> @code {
string LastAction { get; set; }

List <string> splitButtons { get; set; }=new List <string> ()
{
"Reply All",
"Forward",
"Add New Button"
};

void HandleAction(string lastAction)
{
if (lastAction=="Add New Button")
{
splitButtons.Add("New Btn");
}
LastAction=lastAction;
}

void HandleMainBtn()
{
LastAction="Main Btn";
}
} I eagerly await your feedback on whether this aligns with your requirements. If it doesn't meet your needs, please know that I am fully available to provide further assistance in order to help you achieve your desired outcome. Regards, Hristian Stefanov Progress Telerik

### Response

**Leland** commented on 15 Aug 2023

Thanks, this puts me on the right track. While adapting this example to my use case, I tried using some static SplitButtonItems after some dynamic SplitButtonItems. <TelerikSplitButton OnClick="@HandleMainBtn"> <SplitButtonContent> Main Button </SplitButtonContent> <SplitButtonItems> @foreach (var splitBtn in splitButtons)
{ <SplitButtonItem OnClick="@(()=> HandleAction(splitBtn))"> @splitBtn </SplitButtonItem> } <SplitButtonItem OnClick="HandleNewBtn"> Add New Button </SplitButtonItem> <SplitButtonItem OnClick="HandleClearBtns"> Clear Buttons </SplitButtonItem> </SplitButtonItems> </TelerikSplitButton> Last action: <strong> @LastAction </strong> @code {
string LastAction { get; set; }=string.Empty;

List <string> splitButtons { get; set; }=new List <string> ()
{
"Reply All",
"Forward"
};

void HandleAction(string lastAction)
{
LastAction=lastAction;
}

void HandleMainBtn()
{
LastAction="Main Btn";
}

void HandleNewBtn()
{
LastAction="Add New Button";
splitButtons.Insert(0, "New Btn");
}

void HandleClearBtns()
{
LastAction="Clear Buttons";
splitButtons.Clear();
}
} As new buttons are added, instead of remaining at the bottom, the New Button and Clear Button options stay as the third and fourth dropdown options, and the final option in the list "Forward" is pushed after them. Then if the list is cleared and new buttons are added again, the new buttons will all be added below. I know this can be worked around by having static SplitButtonItems above dynamic ones, or by including static ones in the list of dynamic items, but is there another way to keep static SplitButtonItems below all the dynamic ones?

### Response

**Hristian Stefanov** commented on 18 Aug 2023

Hi Leland, To ensure that the static SplitButtonItems are below all the dynamic ones, set a " @key " directive of all buttons to a unique value. This will help the Blazor framework distinguish the buttons and their client-side rendering. I've enhanced the approach I initially suggested. Please run and test it to see the result: <TelerikSplitButton OnClick="@HandleMainBtn"> <SplitButtonContent> Main Button </SplitButtonContent> <SplitButtonItems> @{
int index=0;
}
@foreach (var splitBtn in splitButtons)
{ <SplitButtonItem @key="@($" btn { index }")" OnClick="@(()=> HandleAction(splitBtn))"> @splitBtn </SplitButtonItem> index++;
} <SplitButtonItem @key="@($" penultimate-button { index }")" OnClick="HandleNewBtn"> Add New Button </SplitButtonItem> <SplitButtonItem @key="@($" last-button { index ++}")" OnClick="HandleClearBtns"> Clear Buttons </SplitButtonItem> </SplitButtonItems> </TelerikSplitButton> Last action: <strong> @LastAction </strong> @code {
string LastAction { get; set; }=string.Empty;

List <string> splitButtons { get; set; }=new List <string> ()
{
"Reply All",
"Forward"
};

void HandleAction(string lastAction)
{
LastAction=lastAction;
}

void HandleMainBtn()
{
LastAction="Main Btn";
}

void HandleNewBtn()
{
LastAction="Add New Button";
splitButtons.Insert(0, "New Btn");
}

void HandleClearBtns()
{
LastAction="Clear Buttons";
splitButtons.Clear();
}
} Kind Regards, Hristian
