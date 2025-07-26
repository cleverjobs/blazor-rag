# new version for 3.1 release?

## Question

**Mar** asked on 04 Dec 2019

Is a new release coming for 3.1 any time soon? ETA? I'm not pushing -- just trying to plan for the change. Mark

## Answer

**Marin Bratanov** answered on 04 Dec 2019

Hello Mark, We are hoping to release it tomorrow - on the 5th of December 2019. At the moment we are trying to fix some things, because updates on the linker destroyed the WASM flavor. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 05 Dec 2019

Hello Mark, The 2.5.0 release is live and the WASM flavor requires (again) some configurations. You can find updated information about this in the docs: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations.) Regards, Marin Bratanov

### Response

**Heiko** answered on 09 Dec 2019

Hello Marin, I'm a little bit confused that version 2.5.0 still has references to Microsoft.AspNetCore.Blazor version 3.1.0-preview4.19579.2. Will this be replaced for official 3.1 release which is available since December 3, 2019? Regards Heiko

### Response

**Marin Bratanov** answered on 09 Dec 2019

Hello Heiko, This is required so we can work with the WASM flavor, it ships as separate packages that are still in preview. You can read more about this here: [https://docs.telerik.com/blazor-ui/upgrade/framework-versions.](https://docs.telerik.com/blazor-ui/upgrade/framework-versions.) So, the "preview" you see is for the WASM flavor, the server-side flavor targets the official 3.1.0 version of the framework, and the WASM packages are not pulled for it. Regards, Marin Bratanov
