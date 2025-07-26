# Where can I download language packs or resource files?

## Question

**Rol** asked on 13 Sep 2020

The demo's only supply a few .resx files. I am sure there are more of them, but I am unable to find them, neither in the Account download page, nor in the docs, or mentioned in the forums.

## Answer

**Marin Bratanov** answered on 13 Sep 2020

Hi Roland, Telerik provides the example .resx localizations you see in the demos. You are free to make your own files and translations. You can, for example, use the Kendo localizations as base, there are some of them here. We are also working on creating a repo dedicated to blazor .resx files where you could contribute such translations too. It requires some legal input first, yet when it is ready, we will link it from our documentation. Regards, Marin Bratanov

### Response

**Drewanz** answered on 21 Oct 2020

Is there any forecast to have such resources files available? The ones pointed out are .js files and not .resx files to incorporate on Blazor as the sample shows. Or where we can contribute to increase the number of .resx files - I am looking for pt-BR, but if it does not exist, I may build it and push onto the repo. Thanks

### Response

**Marin Bratanov** answered on 21 Oct 2020

Hi Drewanz, We are working on this and I am hoping that a repo will be available next week, so you could start working on the localization file, and I will write back here with a link when it is available. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 10 Nov 2020

Hi all, The repo is now available: [https://github.com/telerik/blazor-ui-messages](https://github.com/telerik/blazor-ui-messages) At the time of writing, it contains two translations from customers of ours, and everyone can add their own (just fill in the CLA and open the pull request). Regards, Marin Bratanov

### Response

**Drewanz** answered on 10 Nov 2020

Thanks - I will look at it.

### Response

**Marin Bratanov** answered on 10 Nov 2020

@Drewanz - if you have completed the pt-BR translations you're working, you can sign the CLA form and open the pull request. We generally award contributions with Telerik points too. Regards, Marin Bratanov

### Response

**insomnia** answered on 01 Feb 2024

If the languages ​​appear in the local demo, the repository could automatically include them too... ;D [https://github.com/telerik/blazor-ui-messages/pull/31](https://github.com/telerik/blazor-ui-messages/pull/31) Demo still use deprecated package, Should you upgrade to Microsoft.Extensions.Localization (8.0.1) and Microsoft.AspNetCore.Localization (2.2.0)?

### Response

**Dimo** commented on 02 Feb 2024

@insomnia The blazor-ui-messages repository contains . resx files that are provided and maintained by our community. We don't mix our own localization files with community files, as this can lead to misunderstandings. On the other hand, we can consider ways to expose our built-in localization files, so that there is no need to download the whole demo site.

### Response

**insomnia** commented on 05 Feb 2024

Isn't the translation already done by Progress in the demo a good starting point?

### Response

**Dimo** commented on 05 Feb 2024

At first glance it is, but can lead to: The need for us to maintain . resx files in two places. Incorrect expectations that we update all . resx files in the telerik-ui-messages repository. (If we don't maintain the Spanish . resx file after adding it) Misleading impression that an outdated . resx file is the only available thing, while we have an up-to-date version in the installer. That's why I mentioned that we will think how to make our localization files more easily accessible and public.
