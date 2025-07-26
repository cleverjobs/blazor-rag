# wasm culture bug?

## Question

**wuwu** asked on 03 Jun 2020

system:windows10 , area:china, blazor wasm test project, when put the code in one page; <TelerikDateTimePicker Value="System.DateTime.Now"> </TelerikDateTimePicker> run with info:"An unhandled error has occurred",but some other controls like grid is OK! is there the Culture setting problem?

## Answer

**Marin Bratanov** answered on 03 Jun 2020

Hello, Could you check if this is what you are facing: [https://feedback.telerik.com/blazor/1460704-calendars-throw-when-non-gregorian-cultures-are-used?](https://feedback.telerik.com/blazor/1460704-calendars-throw-when-non-gregorian-cultures-are-used?) Regards, Marin Bratanov

### Response

**wu** answered on 03 Jun 2020

I put those code in a page ,and call it. then run ,it is ok! and I test the datetimepicker control from the other library using the same running environment,it is OK!

### Response

**wu** answered on 03 Jun 2020

And I test the TelerikCalendar control ,it is OK! so I think the problem is from the textarea of the TelerikDateTimePicker . If the TelerikGrid control bind the date field,if don't use the following: <Template> @((context as WeatherForecast).Date.ToString("MMMM dd, yyyy")) </Template> run,Can't jump the page include the TelerikGrid control!

### Response

**Marin Bratanov** answered on 03 Jun 2020

Hi, I am attaching here a sample WebAssembly app that works fine for me - the DateTimePicker works, and paging in the grid works without any templates. Please modify this to showcase the problem and send it back to me so I can invesetigate. Regards, Marin Bratanov

### Response

**wu** answered on 04 Jun 2020

Ok,I test your project,It is OK. even when I delete these code string cultureName=zh-Hans; var culture=new CultureInfo(cultureName); CultureInfo.DefaultThreadCurrentCulture=culture; CultureInfo.DefaultThreadCurrentUICulture=culture; Run,it is good! But when I create the new project ,It doesn't work. The attachment is the new project.

### Response

**wu** answered on 04 Jun 2020

I can't send the compressed file, here I change the zip file suffix to jpg

### Response

**wu** answered on 04 Jun 2020

Are there the same dropdowan element about TelerikDropDownList and TelerikDateTimePicker, when I use the TelerikDropDownList control,it doesn't work! but your project is OK! the code: <TelerikDropDownList Data="@DdlData" @bind-Value="SelectedItem"> </TelerikDropDownList> @code { protected List<string> DdlData=new List<string>() { "first", "second", "third", "fourth", "fifth" }; protected string SelectedItem { get; set; }="second"; }

### Response

**Marin Bratanov** answered on 04 Jun 2020

Hi, The MainLayout.razor in the project is missing the TelerikRootComponent. You can read more about this here: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration) The dropdownlist issue probably has the same origin - this missing component. Here's how it should look like and it runs fine for me: @inherits LayoutComponentBase <TelerikRootComponent> <div class="sidebar"> <NavMenu /> </div> <div class="main"> <div class="top-row px-4"> <a href="[http://blazor.net"](http://blazor.net") target="_blank" class="ml-md-auto"> About </a> </div> <div class="content px-4"> @Body </div> </div> </TelerikRootComponent> Regards, Marin Bratanov

### Response

**wu** answered on 04 Jun 2020

Good! But it's a little strange that the TelerikRootComponent is required for pop-up controls.

### Response

**Marin Bratanov** answered on 04 Jun 2020

The reason why is explained in the article I linked. Said shortly, Blazor does not provide another way to render elements outside of the current component, that that's a must for popups. Regards, Marin Bratanov

### Response

**wu** answered on 05 Jun 2020

Maybe other control libraries are implemented differently. [https://ant-design-blazor.github.io/zh-CN/components/datePicker](https://ant-design-blazor.github.io/zh-CN/components/datePicker) But how to realize popup Shadow! Current popup controls are easy to mix with the background.

### Response

**Marin Bratanov** answered on 05 Jun 2020

Hi, You could add a box shadow with your own CSS in case the built-in borders are not sufficient for your preferences. At the moment, however, this will target all popups on the page. The following feature would be helpful so you may want to Follow its status: [https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.](https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.) That said, here's a basic example of adding a drop shadow to all our popups (of course, add the preferred rule, this is rather simplistic I generated off a web site for a quick demo): <style>.k-animation-container { -webkit-box-shadow: 20px 20px 10px 10px rgba ( 0, 0, 0, 0.75 ); -moz-box-shadow: 20px 20px 10px 10px rgba ( 0, 0, 0, 0.75 ); box-shadow: 20px 20px 10px 10px rgba ( 0, 0, 0, 0.75 );
}
</style>

<TelerikDatePicker @bind-Value=" @theValue " />
@code{ DateTime theValue { get; set; }
} Regards, Marin Bratanov

### Response

**wu** answered on 08 Jun 2020

According to your method, I realized the shadow,At the same time, the TreeVew control has been affected,and then solved by style range,It's not perfect, though. But Shadows and pop-up animations now don't match,Can I only modify the popup effect?So how to modify popup effect globally?

### Response

**Marin Bratanov** answered on 08 Jun 2020

Hello, When the item I previously linked gets implemented, you will be able to assign custom CSS classes to individual popup elements of individual components so you can style them without affecting others. Regards, Marin Bratanov
