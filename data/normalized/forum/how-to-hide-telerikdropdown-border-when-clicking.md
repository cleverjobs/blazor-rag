# How to hide telerikdropdown border when clicking

## Question

**Jea** asked on 29 Sep 2023

Hi It seems that s deals with k-picker but how to do good css ?

## Answer

**Hristian Stefanov** answered on 29 Sep 2023

Hi Jean-François, To hide the TelerikDropDownList border upon clicking, you can use the following CSS style: <style>.k-picker-solid.k-focus { box-shadow: none;
} </style> <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" Width="300px" @bind-Value="selectedValue"> </TelerikDropDownList> @code {
public class MyDdlModel
{
public int MyValueField { get; set; }
public string MyTextField { get; set; }
}

int selectedValue { get; set; }=3;

IEnumerable <MyDdlModel> myDdlData=Enumerable.Range(1, 20).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
} Please run and test the above sample to see whether the result matches what you are looking for. Regards, Hristian Stefanov Progress Telerik
