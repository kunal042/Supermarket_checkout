import React, { useState } from "react";
import "./Admin.css"

const AddProductForm = ({open , close}) => {
    const [formData, setFormData] = useState({
        name: "",
        price: "",
        discount_quantity: "",
        discount_price: "",
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        // Convert empty values to null
        const dataToSend = {
            name: formData.name,
            price: formData.price,
            discount_quantity: formData.discount_quantity || null,
            discount_price: formData.discount_price || null
        };

        try {
            const response = await fetch("http://127.0.0.1:8000/api/products/", {method: "POST" , body: JSON.stringify(dataToSend), 
                headers: {
                    "content-type": "application/json",
                },
            });
            if(response.id){
                alert("Product added successfully!");
            }else{
                alert("Product Already exist");
            }
            setFormData({ name: "", price: "", discount_quantity: "", discount_price: "" });
        } catch (error) {
            console.error("Error adding product:", error);
            alert("Failed to add product");
        }
    };

    if(open){ return (
        <main className="modal">
        <div className="container">
            <h2 className="title">Add Product</h2>
            <form onSubmit={handleSubmit}>
                    <input type="text" name="name" value={formData.name} placeholder="Name" onChange={handleChange} required />
                <br />
                
                    <input placeholder="Price" type="number" name="price" value={formData.price} onChange={handleChange} required />
                <br />

                <span className="title" style={{marginTop: "-12px"}}>When You give weekly offer</span>
                    <input placeholder="Discounted Quantity (Optional)" type="number" name="discount_quantity" value={formData.discount_quantity} onChange={handleChange} />
                <br />
                
                    <input placeholder="Discounted Price (Optional)" type="number" name="discount_price" value={formData.discount_price} onChange={handleChange} />
                <br />

                <div style={{display: "flex", gap: "5px"}}>
                <button type="submit">Add Product</button>
                <button onClick={() => {
                    close(false);
                }}>Close</button>

                </div>
            </form>
        </div>
        </main>
    )}else{
        return (<></>);
    }
};

export default AddProductForm;
