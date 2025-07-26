# ClientFooterTemplate

## Question

**Mau** asked on 11 Sep 2020

Is it possible to use something like ClientFooterTemplate in blazor? Like it was possible in the MVC grid? Or do we haven to wait for this a little bit longer. Maurice

## Answer

**Marin Bratanov** answered on 11 Sep 2020

Hi Maurice, Our next release (2.17.0) will have column footer templates, you can preview how they will work here. It is important to note that we do not intend to have client templates for components like the grid - the templates will be standard (native) Blazor templates and not client (JS-based) templates. The only foreseeable exception is the chart as it renders entirely on the client to conserve server resources, and so it has some client templates. Regards, Marin Bratanov
