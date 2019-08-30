(response_code, expected_normal_type_response) => {
    /**
     * json response test template for normal type response
     * author: 周恒 - z50003220
     * datetime: 2019/08/14
     * version: 0.0.1
     * ES_version: ES6 script
     * ps: all useful function defined Embedded
    **/
    if(typeof(response_code) !== "number"){
        throw new Error(`expected number not (${typeof(response_code)})`);
    }
    
    
    let real_response = pm.response.text();
    
    let expected_response_type = Array.isArray(expected_normal_type_response) ? "array" : String(typeof(expected_normal_type_response));
    let real_response_type = Array.isArray(real_response) ? "array" : String(typeof(real_response));
    
    if(expected_response_type !== "number" && expected_response_type !== "string" && expected_response_type !== "boolean"){
        throw new Error(`expected number/string/boolean not (${type})`);
    }else if(real_response_type !== expected_response_type){
        throw new Error(`Error in <response type> expected same type as <expected> not (${real_response_type}), check response body`);
    }else{
        /**
         * postman response test template start
        **/
        // pm.test 检测对应函数是否有异常发生,
        // 使用 https://learning.getpostman.com/docs/postman/scripts/test_examples/ 官网测试api可自动抛出对应异常
        // 手动抛出异常为 throw new Error()
        pm.test("response code ok => " + String(response_code), () => {
            pm.response.to.have.status(response_code);
        });
        
        pm.test("response result ok", () =>{
            // validate response
            pm.expect(expected_normal_type_response === real_response).to.be.true;
        });  
    }
};
