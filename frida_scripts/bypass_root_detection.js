// 루팅 관련 클래스 및 파일 탐지 우회
Java.perform(function () {
    // 파일 경로 체크 우회
    var File = Java.use("java.io.File");
    File.exists.implementation = function () {
        var path = this.getAbsolutePath();
        if (path.includes("su") || path.includes("magisk") || path.includes("busybox")) {
            console.log("[⛔] Root 파일 탐지 차단:", path);
            return false;
        }
        return this.exists();
    };

    // 명령어 실행 우회
    var Runtime = Java.use("java.lang.Runtime");
    Runtime.exec.overload("java.lang.String").implementation = function (cmd) {
        if (cmd.includes("getprop") || cmd.includes("which su")) {
            console.log("[⛔] Root 명령어 차단:", cmd);
            throw new Error("Root check blocked");
        }
        return this.exec(cmd);
    };

    // SU 존재 여부 탐지 우회
    var ProcessBuilder = Java.use("java.lang.ProcessBuilder");
    ProcessBuilder.constructor.overload("[Ljava.lang.String;").implementation = function (args) {
        var argsStr = args.join(" ");
        if (argsStr.includes("su")) {
            console.log("[⛔] su 명령 탐지 차단:", argsStr);
            throw new Error("Nope");
        }
        return this.$init(args);
    };

    console.log("[✔] 루팅 탐지 우회 스크립트 적용됨!");
});
