# DropDownList bind-Value with OnRead data load does not bind value selected from code

## Question

**Cla** asked on 28 Apr 2022

I have a TelerikGrid with inline edit and a GridColumn EditorTemplate with a DropDownList loaded with OnRead and binded to the grid row. Now if the ReadCombo method handle read quickly the DropDownList selected item is binded correcty, but if it take some time (4, 5 seconds..) it not bind, this occurs because bind-Value evaluate before ReadCombo populate the DropDownList. If i use the Data property to populate the DropDownList binding work fine, but i need to use OnRead callback to manage pagination, filters ecc.. Here a simple sample to reply the issue: [https://blazorrepl.telerik.com/mQaymWlm40ccwDCE40](https://blazorrepl.telerik.com/mQaymWlm40ccwDCE40) if you comment the line await Task.Delay(10000); all work fine. There is a solution for this problem? Thanks

### Response

**Timothy J** commented on 28 Apr 2022

We have a similar scenario. We bring the control up with Enabled=false until the OnRead is complete, then we set Enabled=true

### Response

**Claudio** commented on 28 Apr 2022

How can you find when read is completed? Disable / Enable the combo during OnRead does not re-evaluate binding

### Response

**Timothy J** commented on 28 Apr 2022

By implementing an EventHandler for the OnRead event. You get your data, then "Enabled=true". You *may* need to call StateHasChanged after that.

### Response

**Claudio** commented on 02 May 2022

I tried enable the dropdown when OnRead completed as you can see in this sample: [https://blazorrepl.telerik.com/wwazaQaC08YwoBaG28](https://blazorrepl.telerik.com/wwazaQaC08YwoBaG28) but it not solve the issue, i think enable the component only when data are ready does not throw binding update.

## Answer

**Dimo** answered on 03 May 2022

Hi Claudio, Timothy, This issue will be resolved in version 3.3.0, due in mid-May. Here is another related public item, which deals with clearing the DropDownList value. Regards, Dimo
