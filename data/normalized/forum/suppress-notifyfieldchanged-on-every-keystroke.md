# Suppress NotifyFieldChanged on every Keystroke.

## Question

**Jon** asked on 26 Nov 2021

Hello, i would like to use this Framewok, but i encountered following roadblock in conjunction with the DI-Framework i am using (SimpleInjector). As the Input-Components fire NotifyFieldChanged on every keystroke and do not use the "normal" way (onEvent -> triggering the IHandleEvent-Interface) of eventpropagation the DI Container can not apply the correct ServiceScope and thus fails to inject the correct services from Blazor. (NavigationManager, AuthenticationStateProvider) If i use OnChange it might work, if this was the only event, which was fired. (Which is not, because still NotifyFieldChanged fires) Please consider to suppress firing NotifyFieldChanged when OnChange is implemented explicitly. Or perhaps use a property "HandleValidationOn"="ValidationTrigger.OnBlur/LostFocus | ValidationTrigger.OnInput | ValidationTrigger.Never" I would take "Never", as i am validating everything in a backend-service which has no knowledge of the UI for better seperation of concerns.

## Answer

**Hristian Stefanov** answered on 01 Dec 2021

Hi Jonathan, The described functionality is in our plans for the next version 2.30.0 (mid-December). We have the following public item for that. Inputs to Validate only in the OnChange event, not on every keystroke That feature will allow you to fire the OnChange on Enter/Blur. There will be also a separate OnInput event that will fire for each keystroke. Regards, Hristian Stefanov
