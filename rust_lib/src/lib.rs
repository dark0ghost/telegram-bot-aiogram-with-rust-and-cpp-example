extern crate cpython;


use cpython::{
    py_module_initializer, py_fn, Python, PyResult
};


pub  fn py_depth_first_search(_py: Python, list: Vec<usize>) ->  PyResult<bool>{
  for i in list{
      println!("{}",i);
  }
    Ok(true)
}


py_module_initializer!(librust_lib, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py,"rust_out",py_fn!(py,py_depth_first_search(list: Vec<usize>)))?;

    Ok(())
});