// Bypass common emulator detection
Java.perform(function () {
    var Build = Java.use("android.os.Build");

    Build.FINGERPRINT.value = "google/sdk_gphone_x86/generic:11/RSR1.210210.001/7005427:userdebug/dev-keys";
    Build.MODEL.value = "Pixel 4";
    Build.MANUFACTURER.value = "Google";
    Build.BRAND.value = "google";
    Build.DEVICE.value = "coral";
    Build.PRODUCT.value = "coral";

    console.log("[+] Build properties spoofed to bypass emulator check");
});

// Bypass Debugger check
Java.perform(function () {
    var Debug = Java.use("android.os.Debug");
    Debug.isDebuggerConnected.implementation = function () {
        console.log("[+] Bypassed Debug.isDebuggerConnected");
        return false;
    };
});
