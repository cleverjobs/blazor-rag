# Upgrading to 1.3 requirements

## Question

**Ric** asked on 11 Jul 2019

Is there anything we need to make sure we are including when we upgrade to 1.3? I go in the nuget and upgrade to 1.3 and try and do a button click which should open a window with a number of Telerik controls and I get an object reference error on the button click, window doesn't open. Set it back to 1.2 error goes away and everything works just fine.

## Answer

**Rick** answered on 11 Jul 2019

I see. I missed adding the new RootComponent to the layout page.

### Response

**Marin Bratanov** answered on 12 Jul 2019

Hi Rick, You are right that the TelerikRootComponent is the new requirement for some popups. The exception, if it is missing, will be better in our next release, I've already committed the better error handling and message to the codebase. Regards, Marin Bratanov
