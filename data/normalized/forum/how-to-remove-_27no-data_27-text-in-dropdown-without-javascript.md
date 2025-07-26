# How to Remove 'No Data' text in Dropdown without javascript?

## Question

**Vis** asked on 05 Nov 2020

Hello Team, Could you please suggest how to remove the 'No Data' text in Dropdown without javascript or Jquery and also please see the attachment.

## Answer

**Vishnu** answered on 06 Nov 2020

Team, Could you please help on the same. Thanks

### Response

**Kristian** answered on 09 Nov 2020

Hello Vishnu, The 'No Data' message comes from the localizer. At this point, the only way to change it is to override the resource for it. Since this may seem to you like a lot of effort, I created a Feature Request for adding an easier way to override the No Data message and added your vote for it. You can follow it here: [https://feedback.telerik.com/blazor/1494454-no-data-template-in-the-dropdownlist](https://feedback.telerik.com/blazor/1494454-no-data-template-in-the-dropdownlist) Until this feature is implemented, here is the workaround: If you already have localization in your project, just set " DropDownList_NoData " key to an empty string in your resources. If you don't have localization, here are the steps you should do: 1. Create a class for your localizer: public class SampleResxLocalizer: ITelerikStringLocalizer { public string this [ string name]
{ get { return GetStringFromResource(name);
}
} public string GetStringFromResource ( string key ) { // this will override only DropDownList_NoData message and it will return other messages as they are if (key==nameof (Messages.DropDownList_NoData))
{ return string.Empty;
} return Messages.ResourceManager.GetString(key, Messages.Culture); ;
}
} 2. Override the existing Localizer. This step should be done when configuring your services after calling " AddTelerikBlazor() ": builder.Services.AddSingleton( typeof (ITelerikStringLocalizer), typeof (SampleResxLocalizer)); Regards, Kristian
