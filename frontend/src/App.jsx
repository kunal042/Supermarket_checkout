import { useEffect, useState } from "react";
import "./App.css";
import AddProductForm from "./Admin";

  
function App() {
  const [sequence, setSequence] = useState("");
  const [total, setTotal] = useState(0);
  const [openmodal, setOpenModal] = useState(false);
  const [products, setProducts] = useState([]);
  const getItems = () => {
    try{
      fetch("http://127.0.0.1:8000/api/productList" , {
        method: "GET",
      }).then((parsedRes) => {return parsedRes.json()}).then((res) => {
        console.log("res", res);
        setProducts(res);
      })
    }catch(e){

    }
  }
  const checkout = () => {
    try{
      fetch(`http://127.0.0.1:8000/api/checkout/?items=${sequence}` , {
        method: "GET"
      }).then((parsedRes) => {return parsedRes.json()}).then((res) => {
        // console.log("api res is: ", res);
        setTotal(res.total_price);
      })
    }catch(e){
      console.log("Something went wrong in api: ", e);
    }
  } 

  useEffect(() => {
    getItems();
  },[]);
  return (
    <div className="page">
      <div className="addProductContainer">
        <button onClick={() => setOpenModal(true)} className="addprodctbtn">
        Add Product
        </button>
      </div>
      <div className="heading" >
        <h4>Select products by clicking buttons A through D, then go to checkout to see your calculated total</h4>
      </div>
      

      <div className="boxContainer">
        {
          products.map((item) => {
            return <div onClick={() => setSequence(sequence + item.name)} className={`box box${item.id%4}`}>
              Product {item.name}
              <span style={{fontSize: "12px"}}>
                price {item.price}
              </span>
              {item?.discount_quantity && item?.discount_quantity !== 0 ? (
                <span style={{fontSize: "12px"}}>
                  offer {item.discount_quantity}{item.name} : ₹ {item.discount_price}
                </span>
              ) : (
                <span style={{fontSize: "12px"}}>
                  No Offer
                </span>
              )}
              
            </div>
          })
        }
      </div>
      <div className="inputBox">
        <input type="text" value={sequence} onChange={(e) => setSequence(e.target.value)} readOnly  />
        <button onClick={() => {setSequence("");setTotal(0)}}>Reset Sequence</button>
        <button onClick={checkout}>Checkout</button>
      </div>


      <div className="price">
        {`Total Price : ₹ ${total}`}
      </div>


      <AddProductForm open={openmodal} close={setOpenModal}/>
    </div>
  );
}

export default App;

