# Change the command button content base on row value

## Question

**Wil** asked on 14 Nov 2019

I'm trying to change the content of a GridCommandButton based upon a value from the current row - I was thinking it would be something like this: <GridCommandButton Command="Custom" Icon="edit" OnClick="@DisableIntegrator"> <Template> @{ var integrator=context as Integrator; integrator.IsActive ? "Deactivate" : "Activate"; } </Template> </GridCommandButton>

## Answer

**Marin Bratanov** answered on 18 Nov 2019

Hi William, Please Vote for and Follow the feature request that will enable this here: [https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.](https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.) In the meantime, since this seems to invoke some custom method, you can do this for a button in the Template of a regular column, not in a command column. The downside is that it will require two columns until the feature above gets implemented. Regards, Marin Bratanov
