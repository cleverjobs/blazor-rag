# Unsafe content security policy

## Question

**Bra** asked on 26 Apr 2023

We are currently updating our security, and need to tighten content security policy, blocking the use of script-src 'unsafe-eval' & style-src 'unsafe-inline'. We noticed that Telerik UI for Blazor will not work correctly when these policies are applied, as specified in the docs [https://docs.telerik.com/blazor-ui/troubleshooting/csp.](https://docs.telerik.com/blazor-ui/troubleshooting/csp.) It is mentioned that "Some of the above-listed limitations will be addressed in a future version of Telerik UI for Blazor." Is there a more specific timeline as to when this issue will be solved?

### Response

**Michael** commented on 25 Jul 2023

Hi Bram, Not sure if you have gotten around this. With 3 days of work I managed to download the source code and modify all the blazor components to embed a NONCE. I then pass this down to all components from my _Host file. I have been waiting for years on this, if they did not provide the source code then I would most likely not have stuck around.

### Response

**Dimo** commented on 08 Aug 2023

@Ali - keep an eye on our Telerik Blazor Roadmap (it already includes one CSP task) and the Telerik Blazor Release notes. It's possible that we release CSP-related enhancements as early as 4.5.0 or 4.6.0, which are our next two releases.

## Answer

**Dimo** answered on 28 Apr 2023

Hi Bram, We have such a work item for late 2023, but its status is under consideration, so I can't confirm anything officially. Regards, Dimo Progress Telerik

### Response

**Ali** commented on 08 Aug 2023

Hi, Awaiting official confirmation for this.
