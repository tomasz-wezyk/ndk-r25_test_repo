from conans import CMake, ConanFile, tools

class testAndroid(ConanFile):
    name = "ndk-r25_test_repo"
    version = "main"
    url = "https://github.com/tomasz-wezyk/ndk-r25_test_repo.git" 
    settings = "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_paths"

    def configure(self):
        del self.settings.compiler.runtime

    def set_definitions(self, definitions):
        definitions["CMAKE_VERBOSE_MAKEFILE"] = True

        if self.settings.os == "Android":
            definitions["ANDROID_NATIVE_API_LEVEL"] = "24"
            definitions["ANDROID_ABI"] = "arm64-v8a"
            definitions["ANDROID_USE_CLANG"] = True

    def source(self):
        self.run(f"git clone --depth 1 {self.url} --branch main --single-branch")

    def build(self):
        cmake = CMake(self, build_type=self.settings.build_type)
        self.set_definitions(cmake.definitions)
        cmake.configure(source_folder=self.name)
        cmake.build()
        cmake.install()

