// File: page.tsx
// Author: Arvid Möller
// Date: 2025-04-25
// Description: This file contains the HTML for the next.js app.  
// Required files: page.module.css, images.d.ts, next.cofig.ts
// Required libraries: void

"use client";

import { useState } from "react";
import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  const [predictedAccount, setPredictedAccount] = useState<string>("");
  const [imageSrc, setImageSrc] = useState('http://localhost:5001/static/shap_bar.png');

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();  // Förhindra vanlig form-submit

    const form = event.currentTarget;
    const formData = new FormData(form);

    // Skicka till Flask-servern
    const response = await fetch("http://localhost:5001/submit", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    console.log(result);  // Debug

    // Spara predicted account i state
    setPredictedAccount(result.pred_value); 

    setImageSrc(`http://localhost:5001/static/shap_bar.png?${new Date().getTime()}`);
  }

  return (
    <div className={styles.page}>
      <header className={styles.header}>
        AutoAccount
      </header>

      <main className={styles.main}>
        <form className={styles.form} onSubmit={handleSubmit}>
          <label className={styles.label}><strong>Supplier</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Supplier1</label>
            <input className={styles.radioButtons} type="radio" name="supplier" value="Supplier1"></input>
            <label className={styles.label}>Supplier2</label>
            <input className={styles.radioButtons} type="radio" name="supplier" value="Supplier2"></input>
            <label className={styles.label}>Supplier3</label>
            <input className={styles.radioButtons} type="radio" name="supplier" value="Supplier3"></input>
            <label className={styles.label}>Supplier4</label>
            <input className={styles.radioButtons} type="radio" name="supplier" value="Supplier4"></input>
            <label className={styles.label}>Supplier5</label>
            <input className={styles.radioButtons} type="radio" name="supplier" value="Supplier5"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Amount</strong></label>
          <input type="number" name="amount"></input>
         
          <br></br>

          <label className={styles.label}><strong>Department</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Department1</label>
            <input className={styles.radioButtons} type="radio" name="department" value="department_1"></input>
            <label className={styles.label}>Department2</label>
            <input className={styles.radioButtons} type="radio" name="department" value="department_2"></input>
            <label className={styles.label}>Department3</label>
            <input className={styles.radioButtons} type="radio" name="department" value="department_3"></input>
            <label className={styles.label}>Department4</label>
            <input className={styles.radioButtons} type="radio" name="department" value="department_4"></input>
            <label className={styles.label}>Department5</label>
            <input className={styles.radioButtons} type="radio" name="department" value="department_5"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Cost Center</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Cost Center1</label>
            <input className={styles.radioButtons} type="radio" name="cost_center" value="CC1"></input>
            <label className={styles.label}>Cost Center2</label>
            <input className={styles.radioButtons} type="radio" name="cost_center" value="CC2"></input>
            <label className={styles.label}>Cost Center3</label>
            <input className={styles.radioButtons} type="radio" name="cost_center" value="CC3"></input>
            <label className={styles.label}>Cost Center4</label>
            <input className={styles.radioButtons} type="radio" name="cost_center" value="CC4"></input>
            <label className={styles.label}>Cost Center5</label>
            <input className={styles.radioButtons} type="radio" name="cost_center" value="CC5"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Project ID</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>ID1</label>
            <input className={styles.radioButtons} type="radio" name="project_id" value="P1"></input>
            <label className={styles.label}>ID2</label>
            <input className={styles.radioButtons} type="radio" name="project_id" value="P2"></input>
            <label className={styles.label}>ID3</label>
            <input className={styles.radioButtons} type="radio" name="project_id" value="P3"></input>
            <label className={styles.label}>ID4</label>
            <input className={styles.radioButtons} type="radio" name="project_id" value="P4"></input>
            <label className={styles.label}>ID5</label>
            <input className={styles.radioButtons} type="radio" name="project_id" value="P5"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Personnel</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>EMP1</label>
            <input className={styles.radioButtons} type="radio" name="personnel" value="EMP1"></input>
            <label className={styles.label}>EMP2</label>
            <input className={styles.radioButtons} type="radio" name="personnel" value="EMP2"></input>
            <label className={styles.label}>EMP3</label>
            <input className={styles.radioButtons} type="radio" name="personnel" value="EMP3"></input>
            <label className={styles.label}>EMP4</label>
            <input className={styles.radioButtons} type="radio" name="personnel" value="EMP4"></input>
            <label className={styles.label}>EMP5</label>
            <input className={styles.radioButtons} type="radio" name="personnel" value="EMP5"></input>
          </div>

          <br></br>
          
          <label className={styles.label}><strong>Reference</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>REF1</label>
            <input className={styles.radioButtons} type="radio" name="reference" value="REF1"></input>
            <label className={styles.label}>REF2</label>
            <input className={styles.radioButtons} type="radio" name="reference" value="REF2"></input>
            <label className={styles.label}>REF3</label>
            <input className={styles.radioButtons} type="radio" name="reference" value="REF3"></input>
            <label className={styles.label}>REF4</label>
            <input className={styles.radioButtons} type="radio" name="reference" value="REF4"></input>
            <label className={styles.label}>REF5</label>
            <input className={styles.radioButtons} type="radio" name="reference" value="REF5"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Tax Percentage</strong></label>
          <input type="number" name="tax_percentage"></input>

          <br></br>

          <label className={styles.label}><strong>City</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Gothenburg</label>
            <input className={styles.radioButtons} type="radio" name="city" value="Gothenburg"></input>
            <label className={styles.label}>Malmö</label>
            <input className={styles.radioButtons} type="radio" name="city" value="Malmo"></input>
            <label className={styles.label}>Stockholm</label>
            <input className={styles.radioButtons} type="radio" name="city" value="Stockholm"></input>
            <label className={styles.label}>Uppsala</label>
            <input className={styles.radioButtons} type="radio" name="city" value="Uppsala"></input>
            <label className={styles.label}>Linköping</label>
            <input className={styles.radioButtons} type="radio" name="city" value="Linkoping"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Crated at</strong></label>
          <input type="datetime-local" name="created_at"></input>

          <br></br>
          
          <label className={styles.label}><strong>Category</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Category1</label>
            <input className={styles.radioButtons} type="radio" name="Test_category" value="Test_category_1"></input>
            <label className={styles.label}>Category2</label>
            <input className={styles.radioButtons} type="radio" name="Test_category" value="Test_category_2"></input>
            <label className={styles.label}>Category3</label>
            <input className={styles.radioButtons} type="radio" name="Test_category" value="Test_category_3"></input>
            <label className={styles.label}>Category4</label>
            <input className={styles.radioButtons} type="radio" name="Test_category" value="Test_category_4"></input>
            <label className={styles.label}>Category5</label>
            <input className={styles.radioButtons} type="radio" name="Test_category" value="Test_category_5"></input>
          </div>

          <br></br>

          <input className={styles.button} type="submit" value="Submit"></input>
        </form>

        <section className={styles.graphContainer}>
          <h2>Prediction</h2>
          <p>Account: {predictedAccount}</p>

          <h2>Feature Importence</h2>
          <Image className={styles.graph} src={imageSrc} width={600} height={393} alt="Feature Importence Graph"/>   {/* Height to width ratio 1,526408450704225352112676056338:1  */}
          <p className={styles.graphText}>A higher SHAP-value means that feature was more relevant in the making of the prediction.</p>
        </section>
      </main>
    </div>
  );
}