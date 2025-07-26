# DateInput cannot handle the dd-MM-yy format

## Question

**Rol** asked on 31 Aug 2020

Every time you try to edit the year part, strange things happen. "20" is not accepted as 2020, "60" not as 1960. Typing in a full year like 2020 is also not accepted. Is this a bug, or am I doing something wrong?

## Answer

**Marin Bratanov** answered on 31 Aug 2020

Hello Roland, Does the online demo work fine for you, as it does for me: [https://demos.telerik.com/blazor-ui/dateinput/overview?](https://demos.telerik.com/blazor-ui/dateinput/overview?) I can enter both 1960 and 2020. In case you are trying to input a two-digit format - I'd advise against that as it produces heuristic issues that I just described in this new section: [https://docs.telerik.com/blazor-ui/components/dateinput/supported-formats#two-digit-year-formats.](https://docs.telerik.com/blazor-ui/components/dateinput/supported-formats#two-digit-year-formats.) Regards, Marin Bratanov

### Response

**Roland** answered on 31 Aug 2020

I am using a 4-digit format as workaround, but 2-digit formats are quite normal over here. That is why most tools and OS-es have cutoff years. Often a floating cutoff year that is 50 years before the current date. So anything below 70 would be 20xx. Or you can have a cutoff year close to a century ago, because you consider dates past more relevant than future dates. .NET has System.Globalization.TwoDigitYearMax.

### Response

**Marin Bratanov** answered on 01 Sep 2020

Hello Roland, I made this feature request page on your behalf where you can Follow the implementation of such a feature: [https://feedback.telerik.com/blazor/1482911-cutoff-year-to-allow-two-digit-year-formats.](https://feedback.telerik.com/blazor/1482911-cutoff-year-to-allow-two-digit-year-formats.) Regards, Marin Bratanov
