# How can I set the language of the components to Dutch?

## Question

**And** asked on 23 Jul 2023

I tried several suggestions, but I don't succeed in this task. I don't need a multi-lingual approach, just simple dutch labels and datetime formatting.

## Answer

**Nadezhda Tacheva** answered on 26 Jul 2023

Hi Andre, As a start, I recommend going through this resource: [https://docs.telerik.com/blazor-ui/globalization/localization.](https://docs.telerik.com/blazor-ui/globalization/localization.) It provides a detailed explanation of how the localization works in the Telerik components for Blazor and how you can enable it in your app. If you do not need a multi-lingual approach, you can just use the Dutch CultureInfo in your application. The messages(labels) are stored in .resx files and each language has a dedicated file. To include Dutch for the components you must add a .resx that contains the needed messages in Dutch. Dutch is not part of our officially supported translations but you can create the transitions yourself. We have a community-driven public repo with messages where you can also commit yours: [https://github.com/telerik/blazor-ui-messages/tree/main/Messages.](https://github.com/telerik/blazor-ui-messages/tree/main/Messages.) As for the date formatting, the components use the culture of the current thread to render the appropriate culture-specific format for dates, numbers, and currency. You may find more details here: [https://docs.telerik.com/blazor-ui/globalization/globalization-formats.](https://docs.telerik.com/blazor-ui/globalization/globalization-formats.) Having this in mind, if the application culture is Dutch, the components in it should show the according formatting. Please let us know if you experience different behavior. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Andre** answered on 27 Jul 2023

Hi Nadezha, Thank you for your information. I will try this (again) ;-) Kind regards, André

### Response

**Nadezhda Tacheva** commented on 31 Jul 2023

Hi Andre, Take your time to configure the localization and please let me know if any other questions appear during the process.
