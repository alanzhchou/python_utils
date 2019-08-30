(response_code, expected_json_type_response) => {
    /**
     * json response test template
     * author: 周恒 - z50003220
     * datetime: 2019/08/14
     * version: 0.0.1
     * ES_version: ES6 script
     * ps: all useful function defined Embedded
    **/
    if(typeof(response_code) !== "number"){
        throw new Error(`expected number not (${typeof(response_code)})`);
    }
    
    let real_response = pm.response.json();
    
    let expected_response_type = Array.isArray(expected_json_type_response) ? "array" : String(typeof(expected_json_type_response));
    let real_response_type = Array.isArray(real_response) ? "array" : String(typeof(real_response));
    
    if(expected_response_type !== "object"){
        throw new Error(`excepted object/json not (${type})`);
    }else if(real_response_type !== expected_response_type){
        throw new Error(`Error in <response type> excepted object/json not (${real_response_type}), check response body`);
    }else{
        /**
         * compare two object or json (including same key order)
         * @param obj1 : one object or json
         * @param obj2 : another object or json
         * @return : true if equals (including same key order), false if not equals
        **/
        let json_equal = (obj1, obj2) => {
            if(Object.keys(obj1).length !== Object.keys(obj2).length){
                return false;
            }else{
                return JSON.stringify(obj1) === JSON.stringify(obj2);
            }
        };
        
        /**
         * postman response template start
        **/
        // pm.test 检测对应函数是否有异常发生,
        // 使用 https://learning.getpostman.com/docs/postman/scripts/test_examples/ 官网测试api可自动抛出对应异常
        // 手动抛出异常为 throw new Error()
        pm.test("response code ok => " + String(response_code), () => {
            pm.response.to.have.status(response_code);
        });
        
        // change expected resonse here**************************************
        pm.test("response result ok", () =>{
            // validate response
            pm.expect(json_equal(expected_json_type_response, real_response)).to.be.true;
        });
    }
};
