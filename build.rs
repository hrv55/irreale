fn main(){
    let lib_name = "test"
    cc::Build::new()
    .file("lib/libtest.c")
    .compile("test");
}