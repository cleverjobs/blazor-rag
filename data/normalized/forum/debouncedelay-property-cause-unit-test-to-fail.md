# DebounceDelay property cause unit test to fail

## Question

**Cla** asked on 08 Mar 2022

I'm integrating bUnit to add unit test to blazor. Now i have a form with some TelerikTextBox and other components with DataAnnotationValidation. Example: <TelerikTextBox Id="txtUserName" @bind-Value="@EditingItem.UserName"></TelerikTextBox> When i set the input value from bUnit with cut.Find("#txtUserName").Input("UnitTest_User"); the binding property EditingItem.UserName is not updated successully due to default value of DebounceDelay property who is set to 150ms. This cause the subsequent validation of the form to fail. I have open an issue on bUnit project with some sample code, thinking originally who was a bUnit issue, but we found who it's related to telerik components: [https://github.com/bUnit-dev/bUnit/discussions/651](https://github.com/bUnit-dev/bUnit/discussions/651) Note iIf i set the property DebounceDelay="0" on the TelerikTextBox the binding and validation work fine, but it require to change all the components to work with tests. I think we need a settings from telerik blazor components who can allow reset DebounceDelay for all components, before run unit test.

## Answer

**Claudio** answered on 04 Apr 2022

Finally i solved using `SetParameterAndRender` to reset `DebouceDelay` for all `TelerikTextBox` inside the component under test: ``` protected void ResetTelerikTextBoxDebounceDelay<T>(IRenderedComponent<T> cut) where T : Microsoft.AspNetCore.Components.IComponent { var txtElements=cut.FindComponents<TelerikTextBox>(); foreach (var txt in txtElements) txt.SetParametersAndRender(parameters=> parameters.Add(p=> p.DebounceDelay, 0)); } ```

### Response

**Svetoslav Dimitrov** answered on 10 Mar 2022

Hello Claudio, I would like to be really honest regarding the behavior you are facing. We have added a default value of 150ms to the DebouceDelay attribute of our inputs in order to improve the performance of the inputs in a complex validation scenario - let's say an editable Grid or a Form. The way it improves the performance is that the ValueChanged event is not fired on every keystroke, but takes multiple keystrokes until the ValueChanged event is fired. An imaginary scenario would be typing TestInput in a TextBox. For the sake of the example, I`d say that it takes 50ms for a single keystroke. With DebouceDelay set to 0, it would fire 9 times until our TestInput string is input and would mean that the validation would trigger 9 times. With DebounceDelay set to 150ms it would fire only 3 times - the first time for the Tes, the second time - tIn, and the last time for the put. This would mean that the validation will trigger three times less and improve the performance. To be really frank we did not develop the components with bUnit in mind, as we have covered our components with end-to-end tests. Could you provide some additional feedback on why you are using the bUnit to trigger validation for the input, rather than using the value from the property bound to the @bind-Value? Regards, Svetoslav Dimitrov

### Response

**Claudio** answered on 10 Mar 2022

Hi Dimitrov, I'm using bUnit as unit / integration test library, as it work against html markup and allow manage elements with css selector. Telerik seem to sponsor this library as stated in [https://bunit.dev/index.html](https://bunit.dev/index.html) and compare as bUnit friendly library (the only one for now) [https://bunit.dev/docs/providing-input/configure-3rd-party-libs.html.](https://bunit.dev/docs/providing-input/configure-3rd-party-libs.html.) Manage test directly with component instance i think is an anti-pattern of bUnit, also i would like to do an "integration" test as it include multiple layer of the application (html + client business logic). A solution could be allow to update the DebounceDelay property during test, i tried with this code but seem not working: var txt=cut.FindComponents<TelerikTextBox>().FirstOrDefault(txt=> txt.Instance.Id=="txtUserName")?.Instance; txt.DebounceDelay=0;

### Response

**Nadezhda Tacheva** answered on 15 Mar 2022

Hi Claudio, I am stepping in the discussion as my colleague, Svetoslav, is currently out of office. Thank you for the additional details you provided! To handle this scenario, the solution can indeed be updating the DebounceDelay property during test. However, this should be done when you are initializing/rendering the component. You may check here for some examples of how to set component parameters in the test - [https://bunit.dev/docs/providing-input/passing-parameters-to-components.html?tabs=csharp.](https://bunit.dev/docs/providing-input/passing-parameters-to-components.html?tabs=csharp.) I hope this information will help you move forward. Please let us know if any other questions appear. Regards, Nadezhda Tacheva
