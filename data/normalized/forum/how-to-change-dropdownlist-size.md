# How to change DropDownList Size?

## Question

**RobRob** asked on 09 Jun 2025

I'm trying to adjust the existing size definitions as outlined here in your docs: [https://www.telerik.com/blazor-ui/documentation/components/dropdownlist/appearance](https://www.telerik.com/blazor-ui/documentation/components/dropdownlist/appearance) I'd like to adjust the definition for sm, md, lg as they don't work well with TailwindCSS settings. For example lg is just a tad too large and md is a tad too small This is lg: This md: I want to match the border size to our standard input text (aka Postal Code example above). I can't seem to find where sm, lg, md are defined? And, is there a relative "simple" way to modify without going down a "custom" theme path? Rob.

## Answer

**Hristian Stefanov** answered on 10 Jun 2025

Hi Rob, If the built-in sm/md/lg options do not cover your desired appearance. You can adjust the DropDownList height by using the CSS shown below: <style>.k-dropdownlist { height: 40px;
} </style> <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue" Width="300px"> </TelerikDropDownList> @code {
public class MyDdlModel
{
public int MyValueField { get; set; }
public string MyTextField { get; set; }
}

int selectedValue { get; set; }

protected override void OnInitialized()
{
selectedValue=3;
}

IEnumerable <MyDdlModel> myDdlData=Enumerable.Range(1, 20).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
} Regards, Hristian Stefanov Progress Telerik

### Response

**Rob** commented on 10 Jun 2025

Perfect, thank you. May I ask where/how do you know all the ".k-" class selectors? Is there a list/documentation somewhere showing them all?

### Response

**Hristian Stefanov** commented on 11 Jun 2025

Hi Rob, Documentation about the k-classes is rarely needed. Normally, a developer will create a custom theme with our Blazor ThemeBuilder to use a different color scheme. This process does not require knowledge about the k-classes. Advanced customization may involve changing the components' sizing, but the k-classes don't participate in this process either. Which leaves just one case when these classes are needed - when you need to tweak a specific element in a specific way. The easier way to do this is to open the browser's web inspector, see what is the CSS class and current styles, and create a custom CSS rule to apply different styles. The number of possible scenarios here is unlimited, so I can't imagine documentation that can be specific and useful enough. Best regards, Hristian

### Response

**Rob** commented on 11 Jun 2025

Hi Hristian, As with most software development work on limited team size and project funding, we currently don't have time to investigate Telerik custom theme builder. It's certainly something we'll consider in the future and likely remove TailwindCSS from the project. BUT, for now your one line adjustment in .k- class selector is working for us ... I do appreciate your information. So there is no "documentation list" for .k- class selector? I guessed some of them by simply using the telerik namespace: I agree it's not ideal, but for now, it's the way forward.

### Response

**Hristian Stefanov** commented on 12 Jun 2025

Hi Rob, Thank you for your feedback. Indeed, there is no documentation list for "k-" class selectors. I can't imagine documentation that can be specific and useful enough, as the number of possible scenarios here is unlimited. At the same time, all "k-" class selectors are visible in the browser's web inspector. I'm also glad that you can move forward using the approach from my first message. Best regards, Hris

### Response

**Rob** commented on 12 Jun 2025

Hi Hris, Is there any way to easily redefine the sm, md, lg values without going the entire "Theme" route? Rob.

### Response

**Hristian Stefanov** commented on 13 Jun 2025

Hi Rob, I can confirm that there is no built-in option to redefine the sm, md, lg values. Instead of relying on them, I still recommend applying a small CSS style to get the desired appearance, as shown in my initial reply. Kind Regards, Hris
