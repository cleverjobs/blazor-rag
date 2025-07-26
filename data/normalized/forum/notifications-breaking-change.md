# Notifications breaking change

## Question

**Ton** asked on 11 Jul 2023

Hello, After updating to 4.3.0 for Blazor, the close button on the notifications seem to be appearing at the bottom left. Thanks, Tony

### Response

**Georgi** commented on 14 Jul 2023

Hello Tony, Thank you for the provided screenshots. Based on the provided information, I am not completely sure what might be causing the unexpected sizing of the icons. Usually, such UI glitches are related to the usage of an outdated theme with a newer version of the Telerik UI for Blazor suite. In case you have generated a theme with our ThemeBuilder tool, you should regenerate it so that it is built using the latest rendering of the components. Here are the steps that you could follow to regenerate a new theme: Launch ThemeBuilder Create a new project Find the folder that contains the old theme Open the dist folder then the scss folder Open the _tokens.css file Check the colors and manually input them in the ThemeBuilder App Download the new theme with the new variable names Swap the old theme with the new one In the case of upgrading a version prior to 4.0.0, the application might be affected by the breaking changes that occurred with the 4.0.0 version. Additionally, could you share the configuration of the Notification component along with the custom CSS rules applied to the success-notification and success-message-body classes? It would be very helpful if you could replicate the issue in this REPL example and send it back to me so that I can investigate it locally and get back to you with suggestions accordingly. Regards, Georgi Yanushev

### Response

**Tony** commented on 14 Jul 2023

Attached is the CSS for the Success Notification and the config

### Response

**Georgi** commented on 17 Jul 2023

Hi Tony, Thank you for the additional information. Based on it, I have updated the REPL example to attempt to replicate the issue locally, yet, I could not observe the dispositioned icon. Can you confirm the same in the sample? It would be very helpful if you could modify the previously mentioned example to reproduce the issue and send it back to me so I can look into it better and come up with suggestions accordingly. Additionally, could you also share the declaration of the TelerikNotification component within the razor file you are using? Regards, Georgi
