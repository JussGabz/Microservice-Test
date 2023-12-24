import React from "react";
import Wrapper from "./Wrapper";

const ProductsCreate = () => {
    return (
        <Wrapper>
            <form>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" name="title"/>
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" name="image"/>
                </div>
                <button className="btn btn-outline-secondary">Save</button>
            </form>
        </Wrapper>
    )
}

export default ProductsCreate