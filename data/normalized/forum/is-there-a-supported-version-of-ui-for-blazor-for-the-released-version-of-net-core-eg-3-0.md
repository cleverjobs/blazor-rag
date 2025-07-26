# Is there a supported version of UI for Blazor for the released version of .Net Core? eg. 3.0 ?

## Question

**Bit** asked on 30 Oct 2019

If one wanted to use .net core 3.0 is there a version of UI for Blazor one could use?

## Answer

**BitShift** answered on 30 Oct 2019

Even if just for server-side projects?

### Response

**Marin Bratanov** answered on 31 Oct 2019

Hi, At the moment, we support only the latest SDK (.NET Core 3.1. Preview 1 at the time of writing). Supporting older versions will require keeping two entirely separate codebases while working on features and fixes in both, and this is not feasible. Such disparity would only get worse the more versions are available. The way the framework evolves will determine what will be possible and supported in the future. Hopefully after the WASM flavor becomes official it will be possible to slow down and work on compatibility with RTM releases only. At the moment, this is not possible. Our next release will have an article in the documentation that will list the supported framework versions so you can use it as a reference. Regards, Marin Bratanov
