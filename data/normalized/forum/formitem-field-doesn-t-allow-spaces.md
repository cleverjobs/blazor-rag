# FormItem Field doesn't allow spaces

## Question

**Noa** asked on 14 Jul 2021

I'm working on a task where the user needs to be able to enter a space in the form field. I have attached an example of the setup code I am currently using. When the user attempts to add a space in the textbox it is simply not accepted and nothing happens. I have been researching this issue and have not found much help available. So my question are: Is there a workaround? Should I be taking a different approach? public string CustomerName
{ get { get return Ship.CustomerName ?? ""; } set { Ship.CustomerName=value; }
}

<FormItems>
<FormItem Field="@nameof(Example.CustomerName)" />
</FormItem> Update: While troubleshooting this issue I learned a couple of things. My input fields were placed inside of the Telerik Panel Bar. This panel bar is preventing / not registering spaces. I looked through the documentation to see if this was intentional and have not found anything. Has anyone encountered any similar issues? If so, what did you use as a workaround? Documentation: [https://docs.telerik.com/blazor-ui/components/panelbar/events](https://docs.telerik.com/blazor-ui/components/panelbar/events)

### Response

**Matthias** commented on 14 Jul 2021

Hi Noah - I am in the process of adding input to some windows where spaces also need to be added. But have no problem: <TelerikForm Model="@_Customer" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit"> <FormItems> <FormItem Field="@nameof(Customer.Name)"></FormItem> <FormItem Field="@nameof(Customer.City)"></FormItem> </FormItems> </TelerikForm> <code> @Result </code> @code { public Customer _Customer { get; set; }=new Customer(); public bool ValidSubmit { get; set; }=false; public string Result { get; set; }=string.Empty; async Task HandleValidSubmit() { ValidSubmit=true; Result=$"{_Customer.Name} {_Customer.City} len{_Customer.Name.Length}"; await InvokeAsync(StateHasChanged); } void HandleInvalidSubmit() { ValidSubmit=false; } public class Customer { public string Name { get; set; } public string City { get; set; } } } Have a look at the attachment - is counting also spaces - sorry is not possible (only as an answer) Post the picture as an answer in a few seconds

## Answer

**Matthias** answered on 14 Jul 2021

The "Name" field has the length 1 (space) you can see in len: 1 Hope this helps you a little bit - I think the problem is somewhere else

### Response

**Radko** answered on 14 Jul 2021

Hello Noah, I can confirm the FormItem does allow the input of empty spaces as shown on our demos. As a next step, you can open a new support ticket where you can send us a runnable demo application where the issue is reproducible and we can further investigate the issue. Regards, Radko Stanev Progress Telerik

### Response

**David** commented on 14 Nov 2022

I'm having what seems to be same problem. If have a Text-Area on a form on a Panel-Bar. When I enter a space in the Text-Area, the Panel-Bar closes without any reason why. I can paste in text that has imbedded spaces and that works well. I'm on 3.6.1 Blazor UI. I've torn out all my hair, so I thought I'd give you a try :( thanks, DavidA

### Response

**Radko** commented on 15 Nov 2022

Hi David, Are you nesting the textarea inside a template within the PanelBar? If so, the event is bubbling, triggering the keyboard navigation of the PanelBar. To resolve this, you should prevent the propagation of said event. Here is an example of this: [https://blazorrepl.telerik.com/mcbvlfEX094thaLA25](https://blazorrepl.telerik.com/mcbvlfEX094thaLA25) Regards, Radko
