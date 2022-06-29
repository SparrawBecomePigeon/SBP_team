using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class scaling : MonoBehaviour
{
    public float speed = 5.0f;
    int i = 0;
    // Start is called before the first frame update
    public GameObject map;
    public GameObject blockPrefab;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetMouseButton(0))
        {
            transform.Rotate(0f, -Input.GetAxis("Mouse X") * speed, 0f, Space.World);
            transform.Rotate(-Input.GetAxis("Mouse Y") * speed, 0f, 0f);
        }
        if(Input.GetKeyDown(KeyCode.Space)){
            GameObject block = Instantiate(blockPrefab);
            block.transform.position = new Vector3 (i, 0, 0);
            block.transform.SetParent(map.transform, false);
            i++;
        }
        
    }
}

