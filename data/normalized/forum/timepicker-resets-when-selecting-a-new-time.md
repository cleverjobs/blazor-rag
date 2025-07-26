# TimePicker resets when selecting a new time

## Question

**Jes** asked on 30 Jun 2020

Hi The problem I am having is, that when I select a HOUR in the list of hours, by clicking on it with the mouse, the hour is updated shortly and then reset to the hours of the DateTime send into the control. That is, the hour in the text box is set for the selected one, and then reset half a second later. The dropdown with hours 'rolls' back to the initial hour. There is the same problem for the Minutes and Seconds When trying the component on the Telerik Blazor DEMO site, that works just fine, but in my solution (running on my own PC which is setup for the Danish Language and Regional settings) it does as above. My demo component for testing this is quite simple: @page "/CodeSamples" <label for="timepicker">Time:</label> <TelerikTimePicker Min="@Min" Max="@Max" Format="HH:mm:ss" @bind-Value="@selectedTime" Id="timepicker"></TelerikTimePicker> <div class="pt-4">The selected time is: @selectedTime?.ToLongTimeString()</div> @code { public DateTime Min=new DateTime(1900, 1, 1, 10, 0, 0); public DateTime Max=new DateTime(1900, 1, 1, 20, 0, 0); private DateTime? selectedTime=DateTime.Now; } Can you help me? :-)

## Answer

**Svetoslav Dimitrov** answered on 30 Jun 2020

Hello Jesper, The first thing we noticed in the code snippet is that the selectedTime lacks public getter and setter, which is the most common issue when data binding misbehaves. As attached file you can see a demo application, which is referencing Telerik UI for Blazor 2.15.0, the culture is set to Danish, the TelerikTimePicker is located in the Index.razor file and the selectedTime has it's getter and setter. Also, as attached file, you can see a screen recording of the execution of the project. You can run the application locally with you and if its working as expected, compare it against your own. Otherwise, make some changes to the project so that the issue is reproducible and we can further investigate the issue. Regards, Svetoslav Dimitrov

### Response

**Jesper** answered on 01 Jul 2020

Hi Svetoslav, Thank you very much for the reply :-) I have tried the solution you made and made changes to my own project. It works now as expected :-D Regards, Jesper
