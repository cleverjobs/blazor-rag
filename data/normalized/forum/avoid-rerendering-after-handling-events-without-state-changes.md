# Avoid rerendering after handling events without state changes

## Question

**RupRup** asked on 21 Feb 2022

In the main MS Blazor docs there is an article Avoid rerendering after handling events without state changes They give an example of using a button click - eg <button @onclick="EventUtil.AsNonRenderingEventHandler<MouseEventArgs>(HandleClick3)"> Select me (Avoids Rerender and uses <code> MouseEventArgs </code> ) </button> private void HandleClick3(MouseEventArgs args)
{
dt=DateTime.Now;

Logger.LogInformation(
"This event handler doesn't trigger a rerender. " +
"Mouse coordinates: {ScreenX}:{ScreenY}",
args.ScreenX, args.ScreenY);
} How can this be applied to say the TelerikNumericTextBox ValueChanged event? For example, the following gives errors <TelerikNumericTextBox T="int" Value="@NumericTextBoxValue" ValueChanged="EventUtil.AsNonRenderingEventHandler<int>(NumericTextBoxChangeHandler)" Min="1" Max="120" Width="120px"> </TelerikNumericTextBox> private void NumericTextBoxChangeHandler(int newValue)
{
Console.WriteLine($"newValue=={newValue}");
NumericTextBoxValue=newValue;
} Is this possible in Telerik Blazor? Or is there another inbuilt mechanism to control which events automatically invokes StateHasChanged?

## Answer

**Nadezhda Tacheva** answered on 24 Feb 2022

Hello Rup, For our components we are tracking where we need to call StateHasChanged() and where we do not, so we can generally reduce unnecessary re-renders. For some events where we are preventing the StateHasChanged() but we consider it may be useful to still call it in certain scenarios, we have exposed a ShouldRender flag, so one can decide how to proceed. Take, for example, the Grid events. However, if you have encountered unnecessary StateHasChanged() firing, it will be useful to share your feedback, so we can check and address it. As for your current scenario - generally speaking, the ValueChanged event fires as a result of every change in the value of the component. The most common case in this regard is to update the component accordingly, so it can show the correct value. However, if you consider it useful to not fire StateHasChanged() in this scenario, you can indeed proceed with the approach suggested in the Microsoft documentation. I tested it on my end and it seems to work as expected. I am sharing the sample via Telerik REPL for Blazor, so you can directly run and test it in the browser - [https://blazorrepl.telerik.com/wGYGmIFP40GCFdRd45.](https://blazorrepl.telerik.com/wGYGmIFP40GCFdRd45.) You can use it as a base to setup your application. I hope this will help you move forward. Please let us know if any further questions appear. Regards, Nadezhda Tacheva

### Response

**Rup** commented on 24 Feb 2022

I originally had same code as you in question but I get the following two errors... CS1662 Cannot convert lambda expression to intended delegate type because some of the return types in the block are not implicitly convertible to the delegate return type

CS0006 Metadata file '....Project.Client.dll' could not be found Ah, just tried <TargetFramework>net6.0</TargetFramework> and it works. I've been testing on <TargetFramework>net7.0</TargetFramework> I take it Telerik Blazor is .NET6.0 only?

### Response

**Nadezhda Tacheva** commented on 01 Mar 2022

Hi Rup, I am glad to find out you managed to get it up and running. We are generally committed to support only LTS versions of the framework rather than preview ones. Therefore, at this stage, .net 7.0 is not yet supported by the UI for Blazor suite. Here you can find a list of all supported versions - Framework Versions Support.
