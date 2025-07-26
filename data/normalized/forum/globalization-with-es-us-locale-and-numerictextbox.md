# Globalization with es-US locale and NumericTextBox

## Question

**Pat** asked on 27 Jul 2023

I am encountering a strange issue and wanted to check with the community on what might be going on. When using a NumericTextBox in a blazor client-side (WebAssembly) app, and switching between en-US and es-US locales, we are seeing the textbox use commas as the decimal separator for es-US, but are expecting it to use period (consistent with .NET's behavior when formatting for the es-US culture and with other sources). The demo here ( Blazor NumericTextBox Demos - Globalization | Telerik UI for Blazor ) formats numbers the same way when selecting Spanish, and based on the currency symbol it seems clear the formatting is using the es-ES locale (.NET behavior is also consistent with this). Is there a known issue where the NumericTextBox for Telerik Blazor uses commas as the decimal separator for the es-US locale, or is this possibly a new issue for which we should just create a bug report? Or, perhaps most likely, does this point to us doing something wrong, like maybe setting the culture to just es or something? If it matters - when the user switches the language in the UI, we are reloading the site and setting CultureInfo.DefaultThreadCurrentCulture and CultureInfo.DefaultThreadCurrentUICulture to a new CultureInfo instance created with name "en-US" or "es-US".

## Answer

**Tsvetomir** answered on 01 Aug 2023

Hi Patrick, I have already provided a response in the other thread of yours with ID: 1617856. I suggest that we continue the communication there if additional questions arise. For visibility, I am pasting the response here, as well: The default number formatting in the Spanish culture is "000.000,00" or "000 000,00". Therefore, the decimal separator is actually the comma. The dot or space is used to separate thousands and millions (which are not required when formatting generic numbers but rather currencies). I have performed several tests locally and the outcome from the format from .NET is the same in the numeric textbox. Please check the screenshot attached. This can be further verified in this REPL example. Since the REPL's internals cannot be configured through the editor, I am setting the culture in the OnInitializedAsync life-cycle event. Additionally, I performed a thorough research and I could not find any sources that state the es-ES culture to be using the dot as a separator. Can you share the sources that you have found and state how the numbers should be formatted? Regards, Tsvetomir Progress Telerik
