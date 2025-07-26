# Regarding High-risk vulnerabilities during veracode source clear scan.

## Question

**Ash** asked on 18 Aug 2023

During veracode source clear scan on a project that has telerik package(3.7.0), the following error is seen. Security With Vulnerable Methods 0 Critical Risk Vulnerabilities 0 High Risk Vulnerabilities 4 Medium Risk Vulnerabilities 3 Low Risk Vulnerabilities 0 Vulnerabilities - Public Data CVE-2019-0981 High Risk Denial Of Service (DoS) System.Private.Uri 4.3.0 CVE-2019-0980 High Risk Denial Of Service (DoS) System.Private.Uri 4.3.0 CVE-2019-0820 High Risk Denial Of Service (DoS) System.Text.RegularExpressions 4.3.0 CVE-2020-1147 High Risk Remote Code Execution (RCE) System.Data.Common 4.3.0 CVE-2019-0657 Medium Risk Authorization Bypass runtime.unix.System.Private.Uri 4.3.0 CVE-2019-0657 Medium Risk Authorization Bypass System.Private.Uri 4.3.0 CVE-2019-0657 Medium Risk Authorization Bypass runtime.win7.System.Private.Uri 4.3.0

## Answer

**Dimo** answered on 12 Sep 2023

Hi Ashna, It's probably worth saying that all these are packages are external to Telerik UI for Blazor and not part of our source code. Product version 3.7.0 is almost one year old and we have made security improvements since then. Please upgrade to the latest version for better scan results. We also upgraded some dependencies in Telerik.DataSource and Telerik.Recurrence recently. The changes will take effect in our next release 4.6.0, which is due in one month. Regards, Dimo Progress Telerik
