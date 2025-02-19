# Getting started with EM&bull;Script

**EM&bull;Script** requires a cross-development environment consisting of _hosted_&thinsp; software tools which will compile and load executable programs onto _target_&thinsp; MCU hardware.&thinsp; For the host, you can use a PC running **Windows**, **Linux**, or **MacOS**; for the target, you can choose any MCU board for which a corresponding {[cb]em$distro} support package already exists.

Before turning to the **EM&bull;Script SDK** (described next), you should first install or upgrade the following tooling environments on your host PC:

|  |  |  |
|:-|:-|:-|
|[Node.js](https://nodejs.org/en/download)|version 18.0.0 or later| execute {[sh]node}&thinsp;{[sh]--version} to verify |
|[VS Code](https://code.visualstudio.com/download)|version 1.90.0 or later| execute {[sh]code}&thinsp;{[sh]--version} to verify |

!!! warning "Do _not_ proceed forward if these verification checks should fail&thinsp;!!!"

=== "Windows"

    If you don't already have a recent version of the **Git Bash** shell, you should also install [Git for Windows](https://gitforwindows.org/).&nbsp;  To verify your setup, ensure that the {[sh]node} and {[sh]code} commands from the previous table operate correctly under **Git Bash**.

    You must also configure {[sh]npm} to use **Git Bash** as its default shell.&thinsp; The following command reflects the _default_&thinsp; installation directory for **Git Bash**:

    <div markdown class="language-text highlight"><pre><code>$ {[sp,em-color-orange]npm config set script-shell 'C:\Program Files\Git\usr\bin\bash'}</code></pre></div>

    Going forward, all command-line examples will presume your use of this shell.


## Software development kit

You'll provision the latest **EM&bull;Script SDK** onto your host PC in three simple steps, each using the **Node Package Manager** {[sh]npm} command delivered as of **Node.js**:

{[bx,1]} &nbsp; prepare a new folder, which we'll logically name {[fn]&laquo;your-sdk&raquo;} going forward<br>
{[bx,2]} &nbsp; install **SDK** tooling and content, plus some 3<sup>rd</sup> party compilers and loaders<br>
{[bx,3]} &nbsp; verify that you can build (and optionally run) a sample **EM&bull;Script** program

Step {[bx,1]} uses the {[sh]npm} command to initialize a newly-created {[fn]&laquo;your-sdk&raquo;} installation folder somewhere on your PC:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][~]}
$ {[sp,em-color-orange]mkdir emscript-sdk; cd emscript-sdk}<br>
{[sp,em-color-blue][~/emscript-sdk]}
$ {[sp,em-color-orange]npm init -y}
  ...<br>
{[sp,em-color-blue][~/emscript-sdk]}
$ &#9646</code></pre></div>

For simplicity, we've elected to use {[fn]~/emscript-sdk} as our logical {[fn]&laquo;your-sdk&raquo;} folder.&thinsp; Feel free to name and locate this folder anywhere in the file system. 

Step {[bx,2]} uses the {[sh]npm} command to populate your current {[fn]&laquo;your-sdk&raquo;} folder with tooling and content comprising the **EM&bull;Script SDK**:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][&laquo;your-sdk&raquo;]}
$ {[sp,em-color-orange]npm install @em-foundation/emscript-sdk}
  ...
added 11 packages, and audited 12 packages in 26s
  ...</code></pre></div>

Use the {[sh]npm list} command with its&thinsp;{[sh]--depth=1} or&thinsp;{[sh]--all} option for more information.

Step {[bx,3]} finally verifies your **EM&bull;Script** installation by building a small program: 

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][&laquo;your-sdk&raquo;]}
$ {[sp,em-color-orange]npm run verify-build}<br>
&gt; emscript-cli@26.1.0 verify-build
&gt; sh -c '(cd workspace; npx emscript-cli build --unit em.core/em.examples.basic/Ex02_BlinkerP.em.ts)'
building ‘em.examples.basic/Ex02_BlinkerP’ ...
    using setup ‘ti.cc23xx://default’ with board ‘LP_EM_CC2340R5’
    executed ‘em$meta’ program, generated ‘main.cpp’ using [31/62] units in 0.90 seconds
compiling ‘main.cpp’ ...
    image sha32: 1dc95979
    image size: text (1212) + const (12) + data (0) + bss (16)
done in 1.80 seconds<br>
{[sp,em-color-blue][&laquo;your-sdk&raquo;]}
$ &#x25AE</code></pre></div>

## Target MCU hardware

The **SDK** contains all tooling needed to compile and load **EM&bull;Script** programs targeting different MCU development boards.&thinsp;  While we encourage you to purchase one of these boards, you can still learn about **EM&bull;Script** by building (but not running) some sample programs.

=== "LP-EM-CC2340R5"

    The Texas Instruments [CC2340R5](https://www.ti.com/product/CC2340R5) wireless MCU features an Arm Cortex-M0+ CPU together with a familiar suite of peripherals &ndash; including a generic 2.4&thinsp;GHz radio with BLE 5.x support.  Texas Instruments also offers an inexpensive [LP-EM-CC2340R5](https://www.ti.com/tool/LP-EM-CC2340R5) evaluation board in their familiar **LaunchPad** format &ndash; available from TI as well as their distributors.

    You should also purchase this [emulator board](https://www.ti.com/tool/LP-XDS110ET) from TI &ndash; unless you already own a "classic" TI LaunchPad with on-board XDS110 support.  In that case, you can easily connect a legacy LP to your new LP-EM-CC2340R5 board using a cable supplied by TI.&thinsp;  If you haven't used an XDS110 before, run the {[fn]&laquo;your-sdk&raquo;/tools/ti-uniflash/one_time_setup} script.

    We'll soon verify that your LP-EM-CC2340R5 hardware works in concert with the **SDK** by building _and_&thinsp; loading our sample **EM&bull;Script** program.
    
## VS Code extension

To flatten your learning curve, we strongly encourage using our **EM&bull;Script Extension** which you can install by first launching **VS Code**:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][&laquo;your-sdk&raquo;]}
$ {[sp,em-color-orange]code .}</code></pre></div>

Once inside, you'll see a top-level listing of {[fn]&laquo;your-sdk&raquo;} folder.&thinsp; From here, right-click on the {[fn].vsix} file and select **Install Extension VSIX**:

<figure markdown id="fig1">
![Image info](../assets/fig-setup-1.png)
<figcaption>EM&bull;Script Extension Installation
</figure>

If all goes well, you should now see a clickable-item in the **VS Code** status bar which confirms the full version of the **EM&bull;Script** extension currently active.

<figure markdown id="fig2">
![Image info](../assets/fig-setup-2.png)
<figcaption>EM&bull;Script Extension Version
</figure>

From here, you can drill-down into the {[fn]&laquo;your-sdk&raquo;/workspace} sub-folder and explore the software content which **EM&bull;Script** can build and load onto your target MCU hardware.

<figure markdown id="fig3">
![Image info](../assets/fig-setup-3.png)
<figcaption>EM&bull;Script Target Content
</figure>

Our **EM&bull;Script** extension supports features already familiar to **VS Code** users &ndash; syntax highlighting, code navigation, outline views, hover help, intellisense completion, and many more.

## Command line

The **SDK** contains an {[sh]emscript} command-line tool which compiles and loads programs for your target MCU hardware.&thinsp; Used internally by {[sh]npm}&thinsp;{[sh]run}&thinsp;{[sh]verify-build} as part of installation step {[bx,3]}, you can access the {[sh]emscript} command directly from your PC's shell.

You'll find the {[sh]emscript} executable in {[fn]&laquo;your-sdk&raquo;/node_modules/emscript-cli/bin/}.&thinsp; Add this folder to your {[sh]$PATH} or else reference {[sh]emscript} with a named link or alias.&thinsp; To verify:

<div markdown class="language-text highlight"><pre><code>$ {[sp,em-color-orange]emscript --version}
26.1.0.202502161325</code></pre></div>

The {[sh]emscript}&thinsp;{[sh]build} sub-command will serve as your primary entry-point when working with **EM&bull;Script**.&thinsp; Typically invoked inside the {[fn]&laquo;your-sdk&raquo;/workspace} sub-folder, let's now build the _same_&thinsp; target program used to verify the SDK installation:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][&laquo;your-sdk&raquo;/workspace]}
$ {[sp, em-color-orange]emscript build --unit em.core/em.examples.basic/Ex02_BlinkerP.em.ts}
building ‘em.examples.basic/Ex02_BlinkerP’ ...
    using setup ‘ti.cc23xx://default’ with board ‘LP_EM_CC2340R5’
    executed ‘em$meta’ program, generated ‘main.cpp’ using [31/62] units in 0.90 seconds
compiling ‘main.cpp’ ...
    image sha32: 1dc95979
    image size: text (1212) + const (12) + data (0) + bss (16)
done in 1.80 seconds</code></pre></div>

To confirm operation of your target MCU hardware, simply append the {[sh]--load} option to the same command:

<div markdown class="language-text highlight"><pre><code>{[sp,em-color-blue][&laquo;your-sdk&raquo;/workspace]}
$ {[sp, em-color-orange]emscript build --unit em.core/em.examples.basic/Ex02_BlinkerP.em.ts --load}
building ‘em.examples.basic/Ex02_BlinkerP’ ...
  ...
done in 1.80 seconds
loading ‘em.examples.basic/Ex02_BlinkerP’ ...
done</code></pre></div>

If you now see an on-board (green) LED blink five times, go out and celebrate.... :beers:

{[hc]}

