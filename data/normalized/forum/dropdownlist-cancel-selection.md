# DropDownList cancel selection

## Question

**Lou** asked on 17 Jun 2023

Hello. I need to cancel a user selection based on some criteria. Any idea? Example, User choose a new item in the dropdownlist and after check something in OnChange event I want to keep the original selection. <TelerikDropDownList Data="@infosEtapeMaitriseCategories" @bind-Value="@CurrentlyEditingEtapeMaitrise.tlkpEtapeMaitriseCategorieId" TextField="TextField" ValueField="ValueField" Enabled="@tlkpEtapeMaitriseCategorieIdEnabled" Width="100%">

## Answer

**Hristian Stefanov** answered on 19 Jun 2023

Hi Louis, I can confirm that achieving the desired result is possible by utilizing the OnChange event. To demonstrate how to cancel a selection based on a condition, I have prepared an example for you: <TelerikButton OnClick="@TurnOnSelectThird" Enabled="@(!selectThirdOn)"> Turn on - Selecting the third option </TelerikButton> <TelerikDropDownList Data="@MyList" OnChange="@MyOnChangeHandler" @bind-Value="@MySelectedItem" Width="300px" /> @code {
bool selectThirdOn=false;
string MySelectedItem { get; set; }="second";

void MyOnChangeHandler(object theUserInput)
{
if (theUserInput.ToString()=="third" && !selectThirdOn)
{
MySelectedItem="second";
}
}

void TurnOnSelectThird()
{
selectThirdOn=true;
}

protected List <string> MyList=new List <string> () { "first", "second", "third" };
} Please run the provided sample and test it using the following steps: Open the dropdown. Select the third option. (you will notice that it is not selectable) Click the "Turn on - Selecting the third option" button. Try to select the third option again. I hope this example meets your requirements. If there is anything I may have overlooked or if you need a more suitable solution, please let me know, and I will gladly assist you further. Regards, Hristian Stefanov
