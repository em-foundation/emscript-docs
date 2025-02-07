# Getting started with EM&bull;Script

**EM&bull;Script** requires a cross-development environment comprising _hosted_&thinsp; software tools will compile and load executable programs onto _target_&thinsp; MCU hardware.&thinsp; For the host, you'll use a PC running **Windows**, **Linux**, or **MacOS**; for the target, you can choose any MCU board for which an **EM&bull;Script** support package already exists.

Before turning to the **EM&bull;Script SDK** (described next), you should first install or upgrade the following tooling environments on your host PC:

|  |  |  |
|:-|:-|:-|
|[Node.js](https://nodejs.org/en/download)|version 16.3.0 or later| execute {[sh]node}&thinsp;{[sh]--version} to verify |
|[VS Code](https://code.visualstudio.com/download)|version 1.80.0 or later| execute {[sh]code}&thinsp;{[sh]--version} to verify |

=== "Windows"

    If you don't already have a recent version of the **Git Bash** shell, you should also install [Git for Windows](https://gitforwindows.org/).&nbsp;  To verify your setup, ensure that the {[sh]node} and {[sh]code} commands from the previous table operate correctly under **Git Bash**. 

!!! warning "Do _not_ proceed forward if these verification checks should fail&thinsp;!!!"


## Software development kit

The **EM&bull;Script SDK** brings together two complementary elements:

{[bx,1]} &nbsp; a **Git** [repository](https://github.com/em-foundation/emscript-content), which bundles portable as well as MCU-specific target content<br>
{[bx,2]} &nbsp; a **VS Code** [extension](https://marketplace.visualstudio.com/items?itemName=the-em-foundation.em-builder), which provisions host tooling needed to build target programs<br>

As part of step {[bx,1]}, **Zig&bull;EM** currently requires version 0.13.0 of Zig.&thinsp; Once you've added the {[fn]zig} executable to your OS path, invoke {[sh]zig version} from the command-line to confirm.

In step {[bx,2]}, an initial {[sh]git clone} and subsequent {[sh]git pull} of the {[fn]zigem-sdk} repository will download the latest release of **Zig&bull;EM**.

Step {[bx,3]} then builds and installs all additional tooling required by **Zig&bull;EM**.&thinsp; As a final test, invoke {[sh]zig build verify} to compile a small example program found in the SDK.

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-sdk]}
$ {[sp,em-color-orange]zig build verify}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
compiling TARG ...
    image sha: b64cd736z
    image size: text (1168) + const (0) + data (0) + bss (4)
done in 4.57 seconds</code></pre></div>

!!! zig "A mixed build environment"

    While the {[cf]zigem-sdk} repository contains a `build.zig` and `build.zig.zon` file normally used with the {[sh]zig} command, the **Zig&bull;EM SDK** currently depends upon legacy command-line tools like {[sh]make}.&thinsp; Migrating to a pure {[sh]zig build} environment for **Zig&bull;EM** remains our long-term objective. 

=== "Windows"

    You should install [Git for Windows](https://gitforwindows.org/)&thinsp;, which contains the **Git Bash** shell as well as a suite of command-line {[sh]&ast;nix} tools.&thinsp; You should also install this version of [make](https://gnuwin32.sourceforge.net/packages/make.htm) and add this tool to your **Git Bash** {[fn]PATH}.

## Target MCU hardware

The SDK contains all tooling needed to compile and load **Zig&bull;EM** programs targeting different MCU development boards.&thinsp;  While we encourage you to purchase one of these boards, you can still learn about **Zig&bull;EM** by building (but not running) some sample programs.

=== "LP-EM-CC2340R5"

    The Texas Instruments [CC2340R5](https://www.ti.com/product/CC2340R5) wireless MCU features an Arm Cortex-M0+ CPU together with a familiar suite of peripherals &ndash; including a generic 2.4&thinsp;GHz radio with BLE 5.x support.  Texas Instruments also offers an inexpensive [LP-EM-CC2340R5](https://www.ti.com/tool/LP-EM-CC2340R5) evaluation board in their familiar **LaunchPad** format &ndash; available from TI as well as their distributors.

    You should also purchase this [emulator board](https://www.ti.com/tool/LP-XDS110ET) from TI &ndash; unless you already own a "classic" TI LaunchPad with on-board XDS110 support.  In that case, you can easily connect a legacy LP to your new LP-EM-CC2340R5 board using a cable supplied by TI.&thinsp;  If you haven't used an XDS110 before, run the {[fn]zigem-sdk/zig-out/tools/ti-uniflash/one_time_setup} script.

    !!! warning "MacOS users"

        The **Zig&bull;EM SDK** does not automatically provision TI's **UniFlash** loader tool for MacOs.&thinsp; You'll need to manually download [TI-UniFlash](https://dr-download.ti.com/software-development/software-programming-tool/MD-QeJBJLj8gq/8.7.0/uniflash_sl.8.7.0.4818.dmg) and install the application at its default location.

## VS Code extension

To flatten your learning curve, we strongly encourage use of [VS Code](https://code.visualstudio.com/download)&thinsp; [version 1.80.0 or higher] when working with the **Zig&bull;EM** programming framework.

!!! info "Enter {[sh]code --version} from the command-line to verify your current installation."

Once inside **VS Code**, install the latest version of our **Zig&bull;EM Extension** which you'll find in the VS Code marketplace:

<figure markdown id="fig1">
![Image info](/assets/fig-setup-1.png)
</figure>

Our **Zig&bull;EM** extension supports features already familiar to VS Code users &ndash; syntax highlighting, code navigation, outline views, hover help, intellisense completion, and many more.

!!! zig "Interoperability with ZLS and `vscode-zig`"

    The Zig community supports [ZLS](https://github.com/zigtools/zls), which implements Microsoft's [language server protocol](https://microsoft.github.io/language-server-protocol/)&thinsp; for the Zig programming language.&thinsp; The community also publishes a VS Code [Zig Language extension](https://marketplace.visualstudio.com/items?itemName=ziglang.vscode-zig) which uses ZLS.

    **The EM Foundation** maintains its own forks of the community's [zls](https://github.com/em-foundation/zigem-zls) and [vscode-zig](https://github.com/em-foundation/zigem-vscode) repositories, each containing modifications motivated by the **Zig&bull;EM** framework while preserving existing functionality.
    
    At present, however, our **Zig&bull;EM** extension requires you to _disable_&thinsp; the community's Zig Language extension on a per-workspace basis.&thinsp;  Over time, these two VS Code extensions can co-exist.


## Command line

SDK installation step {[bx,3]} called out [above](#software-development-kit) builds and installs {[fn]zigem} &ndash; a command-line tool that lies at the heart of the **Zig&bull;EM** programming framework.&thinsp; You'll find its executable image in the {[fn]zig-out/bin} folder produced through {[sh]zig build}.

!!! info "Consider adding the {[sh]zigem} command to your OS `PATH` or else creating an alias within your shell."

The {[sh]zigem compile} sub-command will serve as a primary entry-point when working with the **Zig&bull;EM** framework.&thinsp; Though not required, you'll typically invoke {[sh]zigem compile}  from within the {[fn]workspace} sub-folder found at the root of the SDK.

To illustrate, let's compile the _same_&thinsp; example program used [earier](#software-development-kit) by {[sh]zig build verify} to test step {[bx,3]} of your SDK installation: 

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-sdk/workspace]}
$ {[sp,em-color-orange]zigem compile --file em.core/em.examples.basic/Ex02_BlinkerP.em.zig}
compiling META ...
    board: LP_EM_CC2340R5
    setup: ti.cc23xx://default
compiling TARG ...
    image sha: b64cd736z
    image size: text (1168) + const (0) + data (0) + bss (4)
done in 4.57 seconds</code></pre></div>

To confirm operation of your target MCU hardware, simply append the {[sh]--load} option to the same command:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][zigem-sdk/workspace]}
$ {[sp,em-color-orange]zigem compile --file em.core/em.examples.basic/Ex02_BlinkerP.em.zig --load}
compiling META ...
    ...
done in 4.57 seconds
loading...
done</code></pre></div>

If you now see an on-board (green) LED blink five times, go out and celebrate.... :beers:

{[hc]}

